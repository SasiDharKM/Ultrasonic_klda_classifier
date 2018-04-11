require(kernlab)
require(lfda)


trainData = read.table("../Flowmeters/rD", sep=" ", header=FALSE)

trainAttr <- trainData[1:43]
trainAttrMatrix <- as.matrix(trainAttr,mode="numeric")

rbfkernel <- rbfdot(sigma = 1)

kGramMatrix <-kernelMatrix(rbfkernel, trainAttrMatrix, trainAttrMatrix)
write.table(kGramMatrix, file = "kGramMatrix.txt", sep = "\t", row.names = FALSE, col.names = FALSE)
trainLabels <- trainData[44:44]
r <- 2
#result comprises of both transformation matrix and transformed data set with less dimensions
result_train <- klfda(kGramMatrix, trainLabels, r, metric="plain")
#result$Z gives transformed dataset matrix and result$T gives the transformation matrix
transformedTrainData  <- result_train$Z
transformationMatrix <- result_train$T
#write.table(transformedTrainData, file = "transformedtraindata.txt", sep = "\t", row.names = FALSE, col.names = FALSE)
write.table(transformationMatrix, file = "transformationMatrix.txt", sep = "\t", row.names = FALSE, col.names = FALSE)

#displaying the transformed dataset 
finalResTrain = cbind(transformedTrainData, trainLabels)
write.table(finalResTrain, file = "../final_data/D_rbf_2R", sep = "\t", row.names = FALSE, col.names = FALSE)

# Check these out for the different kernels
# https://www.rdocumentation.org/packages/kerndwd/versions/2.0.1/topics/kernel%20functions