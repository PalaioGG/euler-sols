// Problem 4
//
// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

function palindrome(n) {
  var number = JSON.stringify(n)
  var itIs = false;

  var middle = Math.floor(number.length/2)

  for(var i = 0; i < middle; i++) {
    if(parseInt(number[i]) == parseInt(number[number.length-(i+1)])) {
      itIs += true;
    }
  }

  return itIs == middle ? true : false;
}

var maxPalindrome = 0;
var mult = 0;
var numbers = [];
for(var i = 0; i < 100; i++) {
  for(var j = 0; j < 100; j++) {
    mult = (900 + i) * (900 + j)
    if(palindrome(mult)) {
      numbers = [(900 + i), (900 + j)]
      maxPalindrome = mult;
    }
  }
}
console.log(numbers)
console.log(maxPalindrome)
