# raise SystemExit 系統終止
driver = input("你有沒有開過車? 有/無")
if driver != "有" and driver != "無":
	print("請輸入有/無")
	raise SystemExit

age = input("那你幾歲?")
age = int(age)

if driver == "有":
	if age > 18:
		print("好喔沒事")
	else:
	    print("抓到了無照駕駛")

elif driver == "無":
	if age > 18:
	    print("快去考")
	else:
	    print("小屁孩")