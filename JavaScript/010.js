// Problem 10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

var limit = 2000000;
// var limit = 10;
var prime = 3;
var sum = 2;

while (prime < limit) {
  timesMultiplied = 0;
  for(var j = Math.round(Math.sqrt(prime)); j >= 1; j--) {
    if( prime % j == 0) {
      timesMultiplied++
    }
  }
  if(timesMultiplied < 2) {
    sum += prime
  }
  prime += 2
}

console.log(sum)
