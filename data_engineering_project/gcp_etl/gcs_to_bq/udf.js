function transform(line){
    let values =  line.split(',');
    let obj = new Object();
    // obj.id = values[0];
    obj.name  = values[0];
    // obj.email = values[2];
    // obj.age  =  values[3];
    obj.city =  values[1];
    let jsonString = JSON.stringify(obj)
    return jsonString
}