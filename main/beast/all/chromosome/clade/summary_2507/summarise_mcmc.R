
peUCLN <- tail(read.table('0.PEUCLN_dates_noHyperPrior.log', head = T), 1000)
mean(peUCLN$meanRate)
mean(peUCLN$treeModel.rootHeight)
