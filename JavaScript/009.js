// Problem 9
//
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// a2 + b2 = c2
//
// For example, 32 + 42 = 9 + 16 = 25 = 52.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

var a, b, c;

for(var n = 2; n < 1000; n++) {
  for(var m = 1; m < n; m++) {
    a = Math.pow(n, 2) - Math.pow(m, 2);
    b = 2*n*m;
    c = Math.pow(n, 2) + Math.pow(m, 2);
    if(Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2) && a + b + c == 1000) {
      var tripletProduct = a * b * c;
    }
  }
}

console.log(tripletProduct)
