setwd("/Users/evandro/Projetos/Kaggle/Competicao_DSA")

library(ggplot2)

df = read.csv("train-pre01.csv")

'''
df$Largest.Property.Use.Type...Gross.Floor.Area..ft...1
class(df$Largest.Property.Use.Type...Gross.Floor.Area..ft...1)

df$X2nd.Largest.Property.Use...Gross.Floor.Area..ft..
class(df$X2nd.Largest.Property.Use...Gross.Floor.Area..ft..)

df$X3rd.Largest.Property.Use.Type...Gross.Floor.Area..ft..
class(df$X3rd.Largest.Property.Use.Type...Gross.Floor.Area..ft..)

df$Total.area..ft.. = df$Largest.Property.Use.Type...Gross.Floor.Area..ft...1 + df$X2nd.Largest.Property.Use...Gross.Floor.Area..ft.. + df$X3rd.Largest.Property.Use.Type...Gross.Floor.Area..ft..
df$Site.Gas..kBtu.ft.. = df$Natural.Gas.Use..kBtu. / df$Total.area..ft..
df$Site.Gas..kBtu.ft..
'''

# ENERGY.STAR.Score x Source.EUI..kBtu.ft..
plot(df$ENERGY.STAR.Score, df$Source.EUI..kBtu.ft.., xlab='Energy Star Score', ylab='Source EUI',type="p")

plot(ENERGY.STAR.Score ~ Source.EUI..kBtu.ft.., data=df, log='x')

qplot(ENERGY.STAR.Score, Source.EUI..kBtu.ft.., data=df, geom="point")

# ENERGY.STAR.Score x Weather Normalized Source.EUI..kBtu.ft..
plot(df$ENERGY.STAR.Score, df$Weather.Normalized.Source.EUI..kBtu.ft.., xlab='Energy Star Score', ylab='Weather N Source EUI',type="p")

plot(ENERGY.STAR.Score ~ Weather.Normalized.Source.EUI..kBtu.ft.., data=df, log='x')

# ENERGY.STAR.Score x Site.EUI..kBtu.ft..
plot(df$ENERGY.STAR.Score, df$Site.EUI..kBtu.ft.., xlab='Energy Star Score', ylab='Site EUI',type="p")

plot(ENERGY.STAR.Score ~ Site.EUI..kBtu.ft.., data=df, log='x')

qplot(ENERGY.STAR.Score, Site.EUI..kBtu.ft.., data=df, geom="point")


# ENERGY.STAR.Score x Site.Gas..kBtu.ft..
plot(df$ENERGY.STAR.Score, df$Site.Gas..kBtu.ft.., xlab='Energy Star Score', ylab='Gas EUI',type="p")

plot(ENERGY.STAR.Score ~ Site.Gas..kBtu.ft.., data=df, log='x')

qplot(ENERGY.STAR.Score, Site.Gas..kBtu.ft.., data=df, geom="point")


# ENERGY.STAR.Score x Electricity.Use.Area..kBtu.ft..
plot(df$ENERGY.STAR.Score, df$Electricity.Use.Area..kBtu.ft.., xlab='Energy Star Score', ylab='Eletricity Used Area',type="p")

plot(ENERGY.STAR.Score ~ Electricity.Use.Area..kBtu.ft.., data=df, log='x')

qplot(ENERGY.STAR.Score, Electricity.Use.Area..kBtu.ft.., data=df, geom="point")

# ENERGY.STAR.Score x GHG.Emissions.Area..Metric.Tons.CO2e.ft..
plot(df$ENERGY.STAR.Score, df$GHG.Emissions.Area..Metric.Tons.CO2e.ft.., xlab='Energy Star Score', ylab='GHG Emissions Area',type="p")

plot(ENERGY.STAR.Score ~ GHG.Emissions.Area..Metric.Tons.CO2e.ft.., data=df, log='x')

qplot(ENERGY.STAR.Score, GHG.Emissions.Area..Metric.Tons.CO2e.ft.., data=df, geom="point")


View(df)

# ENERGY.STAR.Score x Site.EUI..kBtu.ft.. x Site.Gas..kBtu.ft.. x GHG.Emissions.Area..Metric.Tons.CO2e.ft..
camada1 = geom_point(
  mapping = aes(x=ENERGY.STAR.Score, y=Site.EUI..kBtu.ft..),
  data = df,
  size = 3
)
ggplot() + camada1

camada2 <- geom_point(
  mapping = aes(x=ENERGY.STAR.Score, y=Site.Gas..kBtu.ft..),
  data = df,
  color = "red"
)
ggplot() + camada1 + camada2

camada3 <- geom_point(
  mapping = aes(x=ENERGY.STAR.Score, y=GHG.Emissions.Area..Metric.Tons.CO2e.ft..),
  data = df,
  color = "blue"
)
ggplot() + camada1 + camada2 + camada3


# Tentanto pelo tipo da propriedade
camada1 = geom_point(
  mapping = aes(x=ENERGY.STAR.Score, y=Site.EUI..kBtu.ft.., color=Primary.Property.Type...Self.Selected),
  data = df,
  size = 3
)
ggplot() + camada1

unique(df$Primary.Property.Type...Self.Selected)
?unique