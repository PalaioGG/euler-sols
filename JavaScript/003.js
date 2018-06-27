// Problem 3
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

// info: https://www.calculatorsoup.com/calculators/math/prime-factors.php

var target = 600851475143;
var arr = [];

function primeFactor(n, prime) {
  if (n / prime <= 1) {
    arr.push(prime);
    return;
  }

  if (n % prime == 0) {
    arr.push(prime)
    primeFactor(n/prime, prime)
  } else {
    primeFactor(n, prime+1)
  }
}
primeFactor(target, 2)

console.log(arr)
