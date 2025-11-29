def make_album(singer_name,album_name):
    #做个字典
    person = {'singer':singer_name,'album':album_name}
    return person
while True:
    print('\n Tell me the singer and the quanlity of the album')
    print("enter 'q' at any time to quit.")
    singer_name = input('\nWhat is his/her name?')
    if singer_name == 'q':
        break
    album_name = input('How many songs do they create?')
    if album_name == 'q':
        break
singer = make_album(singer_name,album_name)
print(singer)
