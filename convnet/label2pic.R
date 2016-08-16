library(graphics)
library(EBImage)
library(colorspace)

colors <- readRDS("label-color.rds")
predict <- read.table("predict_result.csv", header = F)
names(predict) <- 'label'
predict[,1] <- predict[,1] +1
predict$id <- 1:nrow(predict)
predict <- merge(colors, predict, by = 'label', all.y = TRUE)
predict<- predict[order(predict$id), ]
predict$label <- NULL
predict$id <- NULL

R <- predict$R
G <- predict$G
B <- predict$B

R <- data.frame(matrix(as.vector(R), ncol = 112, byrow = TRUE))
G <- data.frame(matrix(as.vector(G), ncol = 112, byrow = TRUE))
B <- data.frame(matrix(as.vector(B), ncol = 112, byrow = TRUE))

im <- EBImage::readImage("bwtarget.jpg")
im <- channel(im, "rgb")

imageData(im)[,,1] <- as.array(as.matrix(t(R)))
imageData(im)[,,2] <- as.array(as.matrix(t(G)))
imageData(im)[,,3] <- as.array(as.matrix(t(B)))

EBImage::writeImage(x = im, files = "result_plat.jpg")
im <- EBImage::resize(im, 224, 224)
############################
chrominance <- EBImage::resize(im, 224, 224)
luminance <- EBImage::readImage("basic_target(224).jpg")
luminance <- channel(luminance, "rgb")

chrominance_R <- as.vector(as.matrix(imageData(chrominance[,,1])))
chrominance_G <- as.vector(as.matrix(imageData(chrominance[,,2])))
chrominance_B <- as.vector(as.matrix(imageData(chrominance[,,3])))

luminance_R <- as.vector(as.matrix(imageData(luminance[,,1])))
luminance_G <- as.vector(as.matrix(imageData(luminance[,,2])))
luminance_B <- as.vector(as.matrix(imageData(luminance[,,3])))

chrominance_basis <- RGB(chrominance_R, chrominance_G, chrominance_B)
chrominance_basis <- as(chrominance_basis, "LAB")
luminance_basis <- RGB(luminance_R, luminance_G, luminance_B)
luminance_basis <- as(luminance_basis, "LAB")

chrominance_basis <- data.frame(coords(chrominance_basis))
luminance_basis <- data.frame(coords(luminance_basis))

result_basis <- LAB(luminance_basis[,1], chrominance_basis[,2], chrominance_basis[,3])
result_basis <- as(result_basis, "RGB")
result_basis <- data.frame(coords(result_basis))

result_R <- data.frame(matrix(nrow = 224, ncol = 224))
result_G <- data.frame(matrix(nrow = 224, ncol = 224))
result_B <- data.frame(matrix(nrow = 224, ncol = 224))
result_R[,] <- as.vector(as.matrix(result_basis[,1]))
result_G[,] <- as.vector(as.matrix(result_basis[,2]))
result_B[,] <- as.vector(as.matrix(result_basis[,3]))

imageData(im)[,,1] <- as.array(as.matrix(result_R))
imageData(im)[,,2] <- as.array(as.matrix(result_G))
imageData(im)[,,3] <- as.array(as.matrix(result_B))
EBImage::writeImage(x = im, files = "result.jpg")
