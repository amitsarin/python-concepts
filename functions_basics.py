def fahr2celsius(fahr):
    celsius=(5*(fahr-32))/9
    return celsius
print("celsius: ",round(fahr2celsius(99),1))
print("kelvin: ", round(fahr2celsius(99) +273.5,1))

print("--------------------------------------------------")

def say_hello(person1,person2):
    print("hello " + person1 + ",how are you doing ? " + person2 + " is waiting.")
    
say_hello("amit","harsh")
