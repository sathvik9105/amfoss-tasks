const isPrimeNumber = (number) => {
  for (let i = 2; i <= number / 2; i++) {
    if (number % i == 0) {
      return false;
    }
  }
  return true;
};

function* getAllPrimeNumbers(number) {
  for (let i = 2; i <= number; i++) {
    if (isPrimeNumber(i)) yield i;
  }
}

function main() {
  const primeNumberGenerator = getAllPrimeNumbers(23);
  let primeNumber;
  while ((primeNumber = primeNumberGenerator.next().value) !== undefined) {
    console.log(primeNumber);
  }
}

main();