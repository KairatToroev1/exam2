def func(name, **kwargs):
    for i in name:
        print(i)
    for j in kwargs:
        print(f'{j} - {kwargs[j]}')

func(name='USA', population='330 million', is_democratic=True)



def func(name, **kwargs):
    for i in name:
        print(i)
    for j in kwargs:
        print(f'{j} - {kwargs[j]}')


func(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])