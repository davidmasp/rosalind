
# function
edit_distance <- function(x,y,gapPen = 1,misM = 1){
  # initial 0 matrix
  lx = nchar(x)
  ly = nchar(y)
  str_x = unlist(stringr::str_split(x,pattern = ""))
  str_y = unlist(stringr::str_split(y,pattern = ""))
  m = matrix(integer((lx+1)*(ly+1)),ncol = ly+1)
  m[,1] = 0:lx
  m[1,] = 0:ly
  #browser()
  for (i in 2:(lx+1)){
    for (j in 2:(ly+1)){
      distHor = m[i,j-1] + gapPen
      distVer = m[i-1,j] + gapPen
      if (str_x[i-1] == str_y[j-1]){ # -1 is beacause we added up a gap in the m
        distD = m[i-1,j-1]
      } else {
        distD = m[i-1,j-1] + misM
      }
      m[i,j] = min(distHor,distVer,distD)
    }
  }
  return(m[lx+1,ly+1])
}

# code
library(Biostrings)
pt = Biostrings::readAAStringSet(filepath = "test.fasta")
edit_distance(pt[1],pt[2])
