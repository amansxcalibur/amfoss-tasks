const n = parseInt(prompt());
for (let i=0;i<=n; i++) {
    let count=0;
    for (let j=2;j<i;j++) {
        if (i%j==0) {
            count=1;
            break;
        }
    }
    if (i>1 && count==0) {
        console.log(i);
    }
}