// log(n) time complexity - executed in 0.165s

for (let num = 0; num <= 100; num++) {
    if (num % 2 == 0) {
        console.log(num)
    }
}

// log(n/2) time complexity - executed in 0.148s

for (let i = 2; i <= 100; i += 2) {
    console.log(i)
}
