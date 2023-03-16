def drawing():
    print("""
           Fr              m = ?
           |               Fv = ?
           |               μ = ?
         _____
  Fb___ |     |  ___ Fv
________|_____|_______      calculate:
           |                Frez = ?
           |                Fb = ?
           Fsm              a = ?
""")

def Fb(mass, g, μ):
    return round(mass * g * μ,2)

def Frez(Fv, Fb):
    return Fv - Fb

def a(Frez, mass):
    return round(Frez / mass,2)

g = 10

while True:
    drawing()
    print('\nWhat are known values? (Press 000 to exit)')
    mass = float(input('Whats the value of mass? '))
    if mass == 000:
        break

    Fv = float(input('Whats the value of Fv? '))
    μ = float(input('Whats the value of friction coefficient? '))

    Fb_answer = Fb(mass,g,μ)
    Frez_answer = Frez(Fv,Fb_answer)
    a_answer = a(Frez_answer, mass)

    print('\nThe value of Fb is:')
    print(float(mass), '*', int(g), '*', float(μ), '=', Fb_answer)
    
    print('\nThe value of Frez is:')
    print(float(Fv), '-', Fb_answer, '=', Frez_answer)

    print('\nThe value of a is:')
    print(float(Frez_answer), '/', int(mass), '=', a_answer)


