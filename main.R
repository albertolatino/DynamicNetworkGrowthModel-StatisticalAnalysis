#Importing libraries
source("likelihood.R")
source("likelihood.R")
library(igraph)
require("stats4")
require("VGAM")


# Analysis of the degree distribution of the 3 experiments

degree_sequence_preferential = read.table("deg_sequence_preferential.txt",header = FALSE)
degree_sequence_random = read.table("deg_sequence_random.txt",header = FALSE)
degree_sequence_no_growth = read.table("deg_sequence_no_growth.txt",header = FALSE)
sequences <- list(degree_sequence_preferential,degree_sequence_random,degree_sequence_no_growth)
parameters <- matrix(NA, nrow(source), ncol = 9)

for (i in 1:length(sequences)){


  #Degree sequence
  x <- sequences[i]
  print(x)

  # Distribution 1:

  mle_displaced_poisson <- mle(
    minus_log_likelihood_displaced_poisson,
    start = list(gamma = 1),
    method = "L-BFGS-B",
    lower=c(0.0000001)
  )

  # Distribution 2:

  mle_displaced_geometric <- mle(
    minus_log_likelihood_geometric,
    start = list(q = 0.5),
    method = "L-BFGS-B",
    lower=c(0.0000001),
    upper = c(0.9999999)
  )

  # Distribution 3:

  mle_zeta_gamma_2 <-minus_log_likelihood_zeta_gamma_2()

  # Distribution 4:

  mle_zeta <- mle(
    minus_log_likelihood_zeta,
    start = list(gamma = 2),
    method = "L-BFGS-B",
    lower=c(1.0000001)
  )

  # Distribution 5:

  mle_right_truncated_zeta <- mle(
    minus_log_likelihood_truncated_zeta,
    start = list(gamma = 2, kmax = input_table$maxN[i]),
    method = "L-BFGS-B",
    lower=c(1.0000001, input_table$maxN[i])
  )

  # Distribution 6 (Altmann):

  mle_altmann <- mle(
    minus_log_likelihood_altmann,
    start = list(gamma = 2, delta = 0.001),
    method = "L-BFGS-B",
    lower=c(1.0000001, 0.00002)
  )

  parameters[i,] <- c(   i,
                         attributes(summary(mle_displaced_poisson))$coef[1],
                         attributes(summary(mle_displaced_geometric))$coef[1],
                         mle_zeta_gamma_2,
                         attributes(summary(mle_zeta))$coef[1],
                         attributes(summary(mle_right_truncated_zeta))$coef[1], #FOR THIS A Nan Value has been produced
                         attributes(summary(mle_right_truncated_zeta))$coef[2],
                         attributes(summary(mle_altmann))$coef[1],
                         attributes(summary(mle_altmann))$coef[2]
                      )#ALSO THIS

}


