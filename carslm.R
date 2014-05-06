library(datasets)
library(ggplot2)


str(cars)
summary(cars)
head(cars)

lm1 <- lm(dist ~ speed, data = cars)
summary(lm1)

cars.plot <- ggplot(cars, aes(x = speed, y = dist))

cars.plot + geom_point() + stat_smooth(method=lm) + ggtitle("A Linear Model of Cars' Stopping Distances") + xlab("Speed (mph)") + ylab("Stopping Distance (ft)")
