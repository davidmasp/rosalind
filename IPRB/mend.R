
cases <- c("dd","dr","rr")

pind <- c(2,2,2)
pind <- pind 
names(pind) <- cases
t <- sum(pind)

tree <- list()
for (i in cases){
	v1 = pind[i]/t
	tree[[i]] = list()
	for (j in cases){
	  if (i == j){
	    n = pind[j] - 1
	  } else {
	    n = pind[j]
	  }
	 	 nt = t - 1
    v2 <- n/nt
    tree[[i]][[j]] <- v1 * v2
}}

sum(unlist(tree))

sum(unlist(tree$dd)) + tree$dr$dd + (tree$dr$rr * 0.5) + tree$rr$dd + (tree$rr$dr * 0.5) + tree$dr$dr * 0.75








