// Problem 5
//
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

var c = 1;
var n = 2520;

while(n % c == 0 && c <= 20) {
  if(c == 20) {
    console.log(n)
    return;
  }
  c++;
  if (n % c != 0) {
    n++;
    c = 1;
  }
}
