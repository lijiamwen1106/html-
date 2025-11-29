#创建一个用于储存外星人的空列表
aliens = []

#创建30个绿色的外星人
for aliennumber in range(30):
    newalien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(newalien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        print(alien)

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')
#显示创建了多少外星人
print('Total number of aliens:'+str(len(aliens)))
