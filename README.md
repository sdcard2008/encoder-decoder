# A basic customizable encoding and decoding script

**To customize:**
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
}
```
***PS:There is more to the json file. This is used for the example.*** 

Let's say , you want to change the character to reaplace with 'l'


**before , it was ``{"l" : "]"}``** 
```json
 {
    "l" : "]"  
 }
```

**after...** 

```json
{
    "l" : "+"
}
```

**also , you can add more characters , like this:**

```json
{
    "/" : "a",
    "7" : "`"
}
```
