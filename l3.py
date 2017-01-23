package main

import (
"fmt"
"math/rand"
"time"
)

type Token struct {
data string
recipient int //Номер получателя
}

var ch1 chan Token = make(chan Token)
var deep int = 0

func set(t Token) { //Функция передачи в канал
ch1 <- t

}

func get() { // Функция взятия из канала
curToken := <-ch1
go set(curToken)

if deep != curToken.recipient {
deep++
go get()
} else {
fmt.Println("Номер текущего потока: ", deep)
fmt.Println("Токен: ", <-ch1)
}

}
func main() {
rand.Seed(time.Now().UnixNano())
N := rand.Intn(100)
fmt.Println("Номер потока адресата: ", N)

var startToken Token
startToken.recipient = N
startToken.data = "smth data"

go set(startToken)
go get()
time.Sleep(100000000)

}
