# Cytora technical challenge

## How to run

```
git clone git@github.com:Trinkes/cytora_challenge.git
cd cytora_challenge 
docker build -t cytora .
docker run cytora "{\"credit_rating\":1,\"flood_risk\":1,\"revenue\":1}"
```

## Assumptions

For this challenge I assumed that even though the rules are flexible and can change, they won't change very often. I
preferred readability, flexibility, scalability and maintainability over performance and boilerplate code to add or
change new rules.

## input
The docker run command takes a json string as input. The json string should contain the following keys:
- credit_rating
- flood_risk
- revenue
The dictionary values should be numbers.

> :warning: you must escape the json string


## Default implemented rule set
```
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
```