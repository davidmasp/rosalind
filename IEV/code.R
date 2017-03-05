pr = list(
dddd = 1,
dddr = 1,
ddrr = 1,
drdr = 0.75,
drrr = 0.5,
rrrr = 0)

num = c(1,0,0,1,0,1)
num = num * 2
names(num) <- names(pr)
fp = 0
for (i in names(num)){
	fp = fp + (pr[[i]])*num[i]	
}

fp


