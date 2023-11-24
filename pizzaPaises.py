import index

countriesdados = index.getCountries()
dados = index.getDados()

i = 0
while i < len(countriesdados):
  print(countriesdados[i])
  i += 1

# for item in dados:
#     for country in countriesdados:
#         soma = 0
#         if country == item[1] and item[3]:
#             mortes = item[3].split('.') [0]
#             soma = soma + int(mortes)
#     print(soma)
#     print(country)
    #             soma.append(int(mortes))
    # print(sum(soma))




#     new_dado.append(item)
#     if not item[1] in countrys:
#         countrys.append(item[1])

# # for country in countrys:
#     daily_new_deaths = []
# #     daily_new_cases = []

# for dado in new_dado:
#         # if dado[1] == country:
#     mortes = dado[3].split('.') [0]
#     print(mortes)
            # daily_new_deaths += dado[3]
            # daily_new_cases += dado[6]
    # print(daily_new_deaths)
    # print(daily_new_cases)