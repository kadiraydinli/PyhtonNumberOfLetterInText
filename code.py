text = 'This is a test of dictionary. You are supposed to count occurence of each character in this text.';
ar=[]
first=0
second=2
x=0
y=0
top=0
while x<(len(text)/2):
    ar.append(text[first:second])
    y=0
    while y<len(ar):
        if ar[y] == text[first:second]:
            top+=1
        y+=1
    print "\"",text[first:second],"\":", str(top), "tane var"
    top=0
    x+=1
    first+=2
    second+=2
