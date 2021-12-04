library(igraph)

# Here, all negative likelihood functions are listed

minus_log_likelihood_zeta <- function(gamma) {
  length(x) * log(zeta(gamma)) + gamma * sum(log(x))
}

minus_log_likelihood_displaced_poisson<- function(gamma) {

  C <- 0

  for(i in 1:length(x)){
    C <- C + sum(log(2:x[i]))
  }
  -sum(x) * log(gamma)  + length(x) * (gamma + log(1 - exp(-gamma))) + C
}

minus_log_likelihood_geometric <- function(q){

  -(sum(x)-length(x)) * log(1-q) - length(x) * log(q)

}

minus_log_likelihood_zeta_gamma_3 <- function() {
  3 * sum(log(x)) + length(x) * log(zeta(3))
}

minus_log_likelihood_truncated_zeta <- function(gamma,kmax){
  H <-0

  for(i in 1:kmax){
    H <- H + i ^ (-gamma)
  }
  gamma * sum(log(x)) + length(x) * log(H)


}

# Altmann

c_altmann <- function(gamma, delta) {
  k <- c(1:length(x))
  1 / sum(k ^ -gamma * exp(-delta * k))
}

minus_log_likelihood_altmann <- function(gamma, delta) {
  - length(x) * log(c_altmann(gamma, delta)) + gamma * sum(log(x)) + delta * sum(x)
}



get_AIC <- function(m2logL,K,N) {
  m2logL + 2*K*N/(N-K-1) # AIC with a correction for sample size
}

