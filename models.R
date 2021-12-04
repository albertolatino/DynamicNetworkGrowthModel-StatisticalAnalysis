model_0 <- function(a, d=0) {
  a * t + d
}

model_1 <- function (a, d=0) {
  a * t ^ 0.5 + d
}

model_2 <- function (a, b, d=0) {
  a * t ^ b + d
}

model_3 <- function (a, c, d=0) {
  a * exp(c*t) + d
}

model_4 <- function(a, d1, d2=0) {
  a * log(t + d1) + d2
}

aic_nl <- function (n, rss, p) {
  n * log(2*pi) + n * log(rss/n) + n + 2 * (p + 1)
}