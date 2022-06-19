# A basic customizable encoding and decoding script

To customize:
```json
{
    "a" : "=" ,
    "b" : "c" ,
    "c" : "1" ,
    "d" : "l" ,
    "e" : "k" ,
    "f" : "&" ,
    "g" : "{" ,
    "h" : "a" ,
    // so on and so forth
}
```
Let's say , you want to change the character to reaplace with 'l'
** before , it was ``{"l" : "]"}`` **
```json
 {
    // ....
    "l" : "]"
    
    // ....
 }
```

** after... **

```json
{
    "l" : "+"
}
```

** also , you can add more characters , like this: **

```json
{
    "/" : "a",
    "7" : "`"
    // etc etc....
}
```




