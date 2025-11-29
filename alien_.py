favorite_languages = { 
'jen': ['python', 'ruby'], 
 'sarah': ['c'], 
'edward': ['ruby', 'go'], 
'phil': ['python', 'haskell'], 
}
for name,languages in favorite_languages.items():
    if len(favorite_languages.values()) > 1:
        print('\n'+name.title()+"'s favorite language is:")
    else:
        print('\n'+name.title()+"'s favorite language are:")
    for language in languages:
        print('\t'+language.title())
