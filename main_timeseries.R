#Importing libraries
source("models.R")
library(igraph)
library(purrr)
library(qpcR)
require("stats4")
require("VGAM")

timeseries_preferential = readLines("timeseries_preferential.txt")
timeseries_preferential<-strsplit(timeseries_preferential,split=",") #seperate integers by whitespaces
for (i in 1:4) {
  timeseries_preferential[[i]] <- as.integer(timeseries_preferential[[i]])
}

for (i in 1:4) {
  degree_sequence <- timeseries_preferential[[i]]
  time <- seq_along(degree_sequence)

  nls_model_0 <- nls(
    formula = degree_sequence ~ model_0(time, a),
    start = list(a = 1.0)
  )

  nls_model_1 <- nls(
    formula = degree_sequence ~ model_1(time, a),
    start = list(a = 1.0)
  )

  nls_model_2 <- nls(
    formula = degree_sequence ~ model_2(time, a, b),
    start = list(a = 1.0, b = 0.0)
  )

  nls_model_3 <- nls(
    formula = degree_sequence ~ model_3(time, a, c),
    start = list(a = 1.0, c = 0.0)
  )

  nls_model_4 <- nls(
    formula = degree_sequence ~ model_4(time, a, d1),
    start = list(a = 2.0, d1 = 0.1),
    lower = list(d1 = -0.999),
    algorithm = "port"
  )

  nls_model_0p <- nls(
    formula = degree_sequence ~ model_0(time, a, d),
    start = list(a = 1.0, d = 0.0)
  )

  nls_model_1p <- nls(
    formula = degree_sequence ~ model_1(time, a, d),
    start = list(a = 1.0, d = 0.0)
  )

  nls_model_2p <- nls(
    formula = degree_sequence ~ model_2(time, a, b, d),
    start = list(a = 1.0, b = 1.0, d = 0.0)
  )

  # nls_model_3p <- nls(
  #   formula = degree_sequence ~ model_3(time, a, c, d),
  #   start = list(a = 1.0, c = 0.00001, d = 0.00001),
  #   lower = list(c = 0.0),
  #   upper = list(c = 1.0),
  #   algorithm = "port"
  # )

  nls_model_4p <- nls(
    formula = degree_sequence ~ model_4(time, a, d1, d2),
    start = list(a = 2.0, d1 = 0.0000001, d2 = 0.0)
  )
  p <- list(1, 1, 2, 2, 2, 2, 2, 3,
           # 3,
           3)

  models <- list(nls_model_0, nls_model_1, nls_model_2, nls_model_3, nls_model_4,
             nls_model_0p, nls_model_1p, nls_model_2p, nls_model_4p)
  rss <- map(models, RSS)
  aics <- list()
  for (i in seq_along(models)) {
    aics <- append(aics, aic_nl(length(degree_sequence), rss[[i]], p[[i]]))
  }

}