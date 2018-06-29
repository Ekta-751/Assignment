#1.Extract the followings from given Problem.
import re
email1="zuck26@facebook.com"
email2="page33@google.com"
email3="jeff42@amazon.com"
p=re.compile(r"([a-zA-Z0-9].+)@([a-z].+)\.([a-z].+)")
result1=p.findall(email1)
result2=p.findall(email2)
result3=p.findall(email3)
print(result1)
print(result1)
print(result2)
print(result3)

#2.Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
p1=re.compile(r"\b[bB]\w+")
result1=p1.findall(text)
for i in result1:
	print(i)

#3.Split the following irregular sentence into words 
import re 
sentence = "A, very very; irregular_sentence"
p=re.sub(r"[^A-Za-z0-9]"," ",sentence)
print(p)

#4.Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
import re
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
p=re.sub(r"!| RT @TheNextWeb:| http://t.co/lbwej0pxOd cc:|@garybernhardt #rstats"," ",tweet)
print(p) 
