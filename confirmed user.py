#首先，创建一个待验证的用户列表

# 和一个用于储存已验证用户的空列表
unconfirmedusers = ['alice','brain','candance']
confirmedusers = []
#验证每个用户，直到没有未验证用户
#将每个经过验证的列表都移到已验证用户列表中
while unconfirmedusers:
    current_user = unconfirmedusers.pop()
    print('Verify user: '+current_user.title())
    confirmedusers.append(current_user)
#显示所有已验证的用户
print('\nThe following users have been confirmed:')
for confirmeduser in confirmedusers:
    print(confirmeduser.title())
