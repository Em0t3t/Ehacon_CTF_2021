a = "726d1ea6a78c1035d5b97cb6069f2ca0cf0441f6c5e8260eed80bd93db0641679403dbe00a22a94d1676"
res=""
for i in range(0,len(a),2):
    tmp=a[i]+a[i+1]
    if(ord('!')<=int(tmp,16) and int(tmp,16)<= ord('~')):
        res=res+chr(int(tmp,16))
print(res)