# Cytora technical challenge

## How to run

```
git clone 
cd cytora_challenge 
docker build -t cytora .
docker run cytora "{\"credit_rating\":1,\"flood_risk\":1,\"revenue\":1}"
```

## Assumptions

For this challenge I assumed that even though the rules are flexible and can change, they won't change very often. I
preferred readability, flexibility, scalability and maintainability over performance and boilerplate code to add or
change new rules.