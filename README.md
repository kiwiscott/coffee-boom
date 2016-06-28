# coffee-boom


curl -i -H "Content-Type: application/json" -X POST -d '[{"id": "KN200","qty":1},{"id": "KN213","qty":3}]' http://localhost:5555/api/v1.0/reservation

curl -i http://localhost:5555/api/v1.0/orders/24 

curl -i http://localhost:5555/api/v1.0/coffees

curl -i http://localhost:5555/api/v1.0/coffees?query=Big

curl -i -H "Content-Type: application/json" -X POST -d '{"customer":"Read a book"}' http://localhost:5555/api/v1.0/orders
