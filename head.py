head = {
    "value": 5,
    "next": {
        "value": 10,
        "next" : {
            "value": 7,
            "next": None
        }
    }
}


head = {
    "value": 5,
    "next": {
        "value": 5,
        "next": None
    }
}

print(head["next"]["value"])