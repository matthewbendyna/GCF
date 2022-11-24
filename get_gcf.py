import gcf;
import re, sys;

def main():
    numbers=gcf.enterNumbers();
    print(f"Calculating the GCF of inputted values...");
    g_cf=gcf.getGCF(numbers);
    if type(g_cf)==int:
        print(f"The GCF is {g_cf}.");
    else:
        print(g_cf);
    goAgain();

def goAgain():#propt user to perform another calculation or exit program
    yesRx = re.compile("y|yes|ya|yah|yup|positive|definately|absolutely|sure|si", re.IGNORECASE);
    noRx = re.compile("n|no|na|nah|nope|negative|never|hell no", re.IGNORECASE);
    rerun=input("Would you like to calculate another set of numbers? ");
    if re.match(yesRx, rerun):
        main();
    elif re.match(noRx, rerun):
        sys.exit();
    else:
        print("I'm sorry, I couldn't understand that. Please type 'yes' or 'no'.");
        goAgain();

main();