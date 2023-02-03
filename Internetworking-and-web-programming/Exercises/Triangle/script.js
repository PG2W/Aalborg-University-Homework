let result = "";

for (let i = 0; i < 4; i++){
    for (let k = 0; k < 4 - k; k++){
        result += "#";
        console.log(result);
    }
}