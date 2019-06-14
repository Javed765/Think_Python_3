
def print_beam_of_length(n):
    beam = '+ - - - - ' * n 
    print(beam, end = '')
    print('+')
    
print_beam_of_length(4)

def print_pole_of_length(n):
    pole = '|         ' * n
    print(pole, end = '')
    print('|')

def print_grid_of_length(n):
    print_beam_of_length(n)
    print_pole_of_length(n)
    print_pole_of_length(n)
    print_pole_of_length(n)
    print_pole_of_length(n)
    
def print_grid(n, m):
    for i in range (0, (m)):
        print_grid_of_length(n)
    print_beam_of_length(n)

print_grid(1,5)
