# heavenly stems
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp',
        'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']

# earthly branches
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tí', 'Sửu',
        'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

branch = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox',
            'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']

y = int(input('Enter a year: '))

vn = f'{can[y % 10]} {chi[y % 12]}' # Vietnamese
en = branch[y % 12] # English

print(f'Năm {vn}')
print(f'The year of {en}')