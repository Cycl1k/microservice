package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
)

var db *sql.DB

type hist struct {
	ID   string `json:"id"`
	Time string `json:"time"`
}

const serverPort = 8000

func main() {

	var err error

	db, err = sql.Open("postgres", "postgres://userdb:master@127.0.0.1/greetdb2?sslmode=disable")
	if err != nil {
		log.Fatal(err)
	}
	go insert(db)

	router := gin.Default()
	router.GET("/greet/history", getHistory)
	router.GET("/greet", getHello)

	router.Run("127.0.0.1:8080")

}

func insert(db *sql.DB) (int64, error) {
	for {
		time.Sleep(30 * time.Second)
		client := http.Client{}
		resp, err := client.Get("http://127.0.0.1:8000/status")
		CheckError(err)

		var result map[string]interface{}
		json.NewDecoder(resp.Body).Decode(&result)

		f, _ := json.Marshal(result)

		fmt.Println(string(f))

		res, err := db.Exec("INSERT INTO go_connect (time, status) VALUES ($1, $2)", time.Now(), f)
		CheckError(err)

		res.RowsAffected()
	}
}

func getHistory(c *gin.Context) {
	c.Header("Content-Type", "application/json")

	rows, err := db.Query("SELECT id, time FROM go_greet")
	CheckError(err)

	defer rows.Close()

	var go_hist []hist
	for rows.Next() {
		var a hist
		err := rows.Scan(&a.ID, &a.Time)
		CheckError(err)
		go_hist = append(go_hist, a)
	}
	err = rows.Err()
	CheckError(err)

	c.IndentedJSON(http.StatusOK, go_hist)
}

func getHello(c *gin.Context) {
	c.Header("Content-Type", "application/json")

	timeNow := time.Now()

	insertStmt := `insert into "go_greet"("time") values($1)`
	_, e := db.Exec(insertStmt, timeNow.Format("2006-01-02 15:04:05.000000"))

	CheckError(e)

	c.JSON(http.StatusCreated, "Привет от Go!")
}

func CheckError(err error) {
	if err != nil {
		panic(err)
	}
}
