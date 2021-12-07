import random
print("""\
                                        
                 \x1b[1;31m(((((((
                ((((((((((((((((((
              (((((((((####   (((((
             (((((((((((((((     (((\x1b[0m
          ....................   ......
          ....................   ......
          ...../..../..../....
           \x1b[1;32m(((\x1b[0m%#\x1b[1;32m(((((((((\x1b[0m##\x1b[1;32m((\x1b[0m
      \x1b[1;32m((((((\x1b[0m...&&\x1b[1;32m(((((\x1b[0m&&...\x1b[1;32m((((((\x1b[0m
     \x1b[1;32m((((\x1b[0m&\x1b[1;32m(((((\x1b[0m..\x1b[1;32m(((((((\x1b[0m..\x1b[1;32m(((((\x1b[0m&\x1b[1;32m((((\x1b[0m
    \x1b[1;32m(((((\x1b[0m&&\x1b[1;32m(((((((\x1b[0m&&&&&\x1b[1;32m(((((((\x1b[0m&&\x1b[1;32m(((((\x1b[0m
     \x1b[1;32m((((((\x1b[0m&&\x1b[1;32m(((((((((((((((\x1b[0m&&\x1b[1;32m((((((\x1b[0m
        \x1b[1;32m((((((\x1b[0m&&&\x1b[1;32m((((((\x1b[0m#&&&\x1b[1;32m((((((\x1b[0m
            \x1b[1;32m(((((((\x1b[0m&&&\x1b[1;32m(((((((\x1b[0m
                  \x1b[1;32m(((((\x1b[0m

""")

homies=['a', 'b', 'c', 'd', 'e']
copy_homies= homies.copy()

for h in homies:
	k=random.choice([a for a in copy_homies if a != h])
	print(h+' to '+k)
	del copy_homies[copy_homies.index(k)]

