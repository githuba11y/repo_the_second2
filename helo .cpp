#include <iostream>
#include <cmath>

bool isArmstrongNumber(int number) {
    int originalNumber = number;
    int sum = 0;
    int numDigits = static_cast<int>(std::log10(number)) + 1;

    while (number > 0) {
        int digit = number % 10;
        sum += std::pow(digit, numDigits);
        number /= 10;
    }

    return (sum == originalNumber);
}

int main() {
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;

    if (isArmstrongNumber(number)) {
        std::cout << number << " is an Armstrong number." << std::endl;
    } else {
        std::cout << number << " is not an Armstrong number." << std::endl;
    }

    return 0;
}