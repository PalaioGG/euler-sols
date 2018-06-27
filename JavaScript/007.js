// Problem 7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10 001st prime number?

var pos = 10001;
var listOfPrimes = [];
var timesMultiplied;
var prime = 2


while (listOfPrimes.length < pos) {
  timesMultiplied = 0;
  for(var j = prime; j >= 1; j--) {
    if( prime % j == 0) {
      timesMultiplied++
    }
  }
  if(timesMultiplied <= 2) {
    listOfPrimes.push(prime)
  }
  prime++
}
console.log(listOfPrimes[listOfPrimes.length-1])
