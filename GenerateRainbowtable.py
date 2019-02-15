import string
import hashlib
def sha1(word):
    hashword = ""
    hashword = hashlib.sha1(word.encode('utf-8')).hexdigest()
    return  hashword
def generate():
    f = open("10k_common_password.txt","r")
    rb = open("rainbox.txt","w")
    for i in f:
        k = permuteString(i.strip())
        for i in f:
             k = permuteString(i.strip())
             for j in k:
                 rb.write(sha1(j))
                 rb.write(" ")
                 rb.write(j)
                 rb.write("\n")
    rb.close()
    print("Finish")

def permuteString(org):
        if(len(org)==1):
            return permuteChar(org[0])
        tmp = permuteChar(org[0])
        strs=[]
        for s1 in tmp:
                 for s2 in permuteString(org[1:]):
                     strs.append(s1+s2)
        return strs;
def permuteChar(ch):
        if((ch=="i")):
            return("i","I","1")
        if((ch=='l')):
             return("l","L","1")
        if(ch.isalpha()):
             return(ch.lower(),ch.upper())
        return(ch)
print("Start Generate rainbow table:")
generate()
