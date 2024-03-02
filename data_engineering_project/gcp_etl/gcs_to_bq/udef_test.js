function transform(line) {
    var values = line.split(',');
    
    var obj = new Object();
    obj.name = values[0];
    obj.city = values[1];
    var jsonString = JSON.stringify(obj);
    print("jsonString",jsonString)
    return jsonString;
    }