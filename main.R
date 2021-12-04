#Importing libraries
source("likelihood.R")
library(igraph)
require("stats4")
require("VGAM")


# Analysis of the degree distribution of the 3 experiments

degree_sequence_preferential = read.table("deg_sequence_preferential.txt",header = FALSE)
degree_sequence_random = read.table("deg_sequence_random.txt",header = FALSE)
degree_sequence_no_growth = read.table("deg_sequence_no_growth.txt",header = FALSE)
sequences <- list(degree_sequence_preferential, degree_sequence_random, degree_sequence_no_growth)
models <- c("preferential", "random", "no growth")
parameters <- matrix(NA, length(sequences), ncol = 9)
parameters_with_altmann_table <- data.frame("Model" = character(),
                               "(Poisson) λ" = double(),
                               "(Geometric) q" = double(),
                               "(Zeta) γ" = double(),
                               "(R.t. Zeta) γ_1" = double(),
                               "(R.t. Zeta) k_max" = double(),
                               "(Altmann) γ" = double(),
                               "(Altmann) δ" = double(),
                               check.names = FALSE)
aics <- matrix(NA, length(sequences), ncol = 7)
aics_with_altmann_table <- data.frame("Model" = character(),
                         "Displaced Poisson" = double(),
                         "Displaced Geometric" = double(),
                         "Zeta with γ=3" = double(),
                         "Zeta" = double(),
                         "R.t. Zeta" = double(),
                         "Altmann" = double(),
                         check.names = FALSE)
aics_with_altmann_delta_table <- data.frame("Model" = character(),
                               "Displaced Poisson" = double(),
                               "Displaced Geometric" = double(),
                               "Zeta with γ=3" = double(),
                               "Zeta" = double(),
                               "R.t. Zeta" = double(),
                               "Altmann" = double(),
                               check.names = FALSE)

for (i in 1:length(sequences)){


  #Degree sequence
  x <- sequences[i]
  x <- x[[1]]$V1
  maxN <- max(x)
  # print(x)

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

  mle_zeta_gamma_3 <-minus_log_likelihood_zeta_gamma_3()

  # Distribution 4:

  mle_zeta <- mle(
    minus_log_likelihood_zeta,
    start = list(gamma = 3),
    method = "L-BFGS-B",
    lower=c(1.0000001)
  )

  # Distribution 5:

  mle_right_truncated_zeta <- mle(
    minus_log_likelihood_truncated_zeta,
    start = list(gamma = 3, kmax = maxN),
    method = "L-BFGS-B",
    lower=c(1.0000001, maxN)
  )

  # Distribution 6 (Altmann):

  mle_altmann <- mle(
    minus_log_likelihood_altmann,
    start = list(gamma = 2.5, delta = 0.001),
    method = "L-BFGS-B",
    lower=c(1.0000001, 0.00002)
  )

  parameters[i,] <- c(   i,
                         attributes(summary(mle_displaced_poisson))$coef[1],
                         attributes(summary(mle_displaced_geometric))$coef[1],
                         mle_zeta_gamma_3,
                         attributes(summary(mle_zeta))$coef[1],
                         attributes(summary(mle_right_truncated_zeta))$coef[1],
                         attributes(summary(mle_right_truncated_zeta))$coef[2],
                         attributes(summary(mle_altmann))$coef[1],
                         attributes(summary(mle_altmann))$coef[2]
                      )#ALSO THIS

  parameters_with_altmann_table[i, 1] <- models[i]
  parameters_with_altmann_table[i, 2:3] <- parameters[i, 2:3]
  parameters_with_altmann_table[i, 4:6] <- parameters[i, 5:7]
  parameters_with_altmann_table[i, 7:8] <- parameters[i, 8:9]

  aics[i,] <- c(i,
                get_AIC(attributes(summary(mle_displaced_poisson))$m2logL, 1, length(x)),
                get_AIC(attributes(summary(mle_displaced_geometric))$m2logL, 1, length(x)),
                get_AIC(2*mle_zeta_gamma_3, 0, length(x)),
                get_AIC(attributes(summary(mle_zeta))$m2logL, 1, length(x)),
                get_AIC(attributes(summary(mle_right_truncated_zeta))$m2logL, 2, length(x)),
                get_AIC(attributes(summary(mle_altmann))$m2logL, 2, length(x))
  )
  aics_with_altmann_table[i, ] <- aics[i, ]
  aics_with_altmann_table[i, 1] <- models[i]

}

best_aics <- matrix(NA, length(sequences), ncol = 2)
diff_aics <- matrix(NA, length(sequences), ncol = 7)

# creating delta AIC table

for (i in 1:nrow(aics)) {
  best_aics[i, 1] <- aics[i, 1]
  best_aics[i, 2] <- min(as.numeric(aics[i, 2:7]))
}

for (i in 1:nrow(aics)) {
  diff_aics[i, 1] <- aics[i, 1]
  diff_aics[i, 2:7] <- as.numeric(aics[i, 2:7]) - as.numeric(best_aics[i, 2])
}

for (i in 1:nrow(diff_aics)) {
  aics_with_altmann_delta_table[i,] <- diff_aics[i,]
  aics_with_altmann_delta_table[i, 1] <- models[i]
}

