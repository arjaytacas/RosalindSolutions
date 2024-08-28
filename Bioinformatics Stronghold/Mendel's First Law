# read problem here > https://rosalind.info/problems/iprb/

# we have k,m,n which represents AA, Aa, and aa
# we need to check the probability at which the mating organism will produce an offspring displaying the dominant phenotype which is AA or Aa
# if we mate AA x AA, AA x Aa and AA x aa it will always produce an offspring with the dominant allele, Aa x Aa have 75%, 
# Aa x aa have 50% chance and aaxaa have 0

k = 2 #AA
m = 2 #Aa
n = 2 #aa
totpop = k + m + n

# cross breed between AA x AA 
prob1 = (k/totpop)*((k-1)/(totpop-1))
# cross breed between AA x Aa
prob2 = (k/totpop)*(m/(totpop-1)) + (m/totpop)*(k/(totpop-1))
# cross breed between AA x aa
prob3 = (k/totpop)*(n/(totpop-1)) + (n/totpop)*(k/(totpop-1))
# cross breed between Aa x Aa
prob4 = (3/4)*(m/totpop)*((m-1)/(totpop-1)) 
# cross breed between Aa x aa
prob5 = (1/2)*(m/totpop)*(n/(totpop-1)) + (1/2)*(n/totpop)*(m/(totpop-1))

domprob = prob1+prob2+prob3+prob4+prob5

print(round(domprob,5))
