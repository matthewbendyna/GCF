from gcf import getGCF;
import re, sys;

def main():
    exitRx=re.compile(r"q|quit|exit|end|e|terminate|t|leave|l|bye|b|goodbye|gone|g");
    numerator=input("Please enter numerator: ");
    if re.match(exitRx, numerator) or numerator=="":
        sys.exit();
    else:
        n=float(numerator);
        if n%1 != 0:
            print("numerator must be an integer, not a decimal fraction or string of letters/non-digit symbols.");
            main();
    denominator=input("Please enter denominator: ");
    if re.match(exitRx, denominator) or denominator=="":
        sys.exit();
    else:
        d=float(denominator);
        if d%1 != 0:
            print("denominator must be an integer, not a decimal fraction or string of letters/non-digit symbols.");
            main();
    numbers=[numerator, denominator]
    g_cf=getGCF(numbers);
    fnumerator=str(int(int(numerator)/int(g_cf)));
    fdenominator=str(int(int(denominator)/int(g_cf)));
    print(f"{fnumerator}/{fdenominator}");
    main();

print("This program will take two numbers, a numerator(top) and denominator(bottom) and simplify the corresponding fraction using the GCF of both numbers.");
main();