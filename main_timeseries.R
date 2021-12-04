#Importing libraries
source("models.R")
library(igraph)
require("stats4")
require("VGAM")

timeseries_preferential = as.matrix(read.csv("timeseries_preferential.txt", header=FALSE))

for (i in 1:4) {
  t <- timeseries_preferential[i,]

  nls_model_0 <- nls(
    formula = model_0
  )
}