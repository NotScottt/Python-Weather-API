# Python Weather API
This is a REST-API written in Python. <br>

### How to run the API:
1. Copy this repo to a local directory
2. Navigate to [/backend/](https://github.com/NotScottt/Python-Weather-API/tree/main/backend)
3. Run ```server.py```

### How to change Host and Port
You can simply change the host and port before you start the API.<br>
On [line 36](https://github.com/NotScottt/Python-Weather-API/blob/c13c998a256b793509bf1240cdee45f997f6a538/backend/server.py#L36) you can add host and Port as parameters like in the comment below.

### Possible API calls
``` 
http://localhost:5000/weather/current?day=0
```
<details>
  <summary>result</summary>
  
  ``` js
    {
      "condition": "M\u00e4\u00dfig bew\u00f6lkt",
      "date": "12.02.2024",
      "day": "Heute",
      "temp": "9\u00b0C"
    }
  ```
</details>

``` 
http://localhost:5000/weather/all
```
<details>
  <summary>result</summary>
  
  ``` js
    [
  {
    "condition": "M\u00e4\u00dfig bew\u00f6lkt",
    "date": "12.02.2024",
    "day": "Heute",
    "temp": "9\u00b0C"
  },
  {
    "condition": "Leichter Regen",
    "date": "13.02.2024",
    "day": "Dienstag",
    "temp": "8\u00b0C"
  },
  {
    "condition": "Bedeckt",
    "date": "14.02.2024",
    "day": "Mittwoch",
    "temp": "9\u00b0C"
  },
  {
    "condition": "Leichter Regen",
    "date": "15.02.2024",
    "day": "Donnerstag",
    "temp": "12\u00b0C"
  },
  {
    "condition": "Leichter Regen",
    "date": "16.02.2024",
    "day": "Freitag",
    "temp": "12\u00b0C"
  },
  {
    "condition": "Leichter Regen",
    "date": "17.02.2024",
    "day": "Samstag",
    "temp": "12\u00b0C"
  },
  {
    "condition": "M\u00e4\u00dfig bew\u00f6lkt",
    "date": "18.02.2024",
    "day": "Sonntag",
    "temp": "11\u00b0C"
  },
  {
    "condition": "Leichter Regen",
    "date": "19.02.2024",
    "day": "Montag",
    "temp": "12\u00b0C"
  }
]
  ```
</details>
