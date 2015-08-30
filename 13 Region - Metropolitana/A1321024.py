rawdata = open("A1321024.txt")
OutputFile = open("A1321024-v2.txt", 'w')
users = []
OutputFile.write('Nombre' + ';' + 'RUT' + ';' + 'Sexo' + ';' +
                 'Domicilio' + ';' + 'Circunscripcion' + ';' + 'Mesa')
OutputFile.write("\n")
for line in rawdata:
    if len(line) >= 40:
        user = {}
        guion = "-"
        dist1 = "TRINIDAD"
        dist2 = "SAN JOSE DE LA ESTRELLA"
        dist3 = "BELLAVISTA"
        discriminador = "ELECTORAL"
        posdiscriminador = line.find(discriminador,0)
        if posdiscriminador == -1:
            largodist1 = len(dist1)
            largodist2 = len(dist2)
            largodist3 = len(dist3)
            largolinea = len(line)
            posguion = line.find(guion, 20)
            posvar = line.find(" VAR ", 0)
            posmuj = line.find(" MUJ ", 0)
            posdist1 = line.find(dist1, largolinea - 20)
            posdist2 = line.find(dist2, largolinea - 35)
            posdist3 = line.find(dist3, largolinea - 20)
            varesp = " "
            comrut = line.find(varesp, posguion - 11)
            cierremesa = line.find(varesp, largolinea - 4)
            user['nombre'] = line[0: posguion - 10].strip()
            user['rut'] = line[comrut:posguion + 2].strip()

            if posvar == -1:
                user['sexo'] = line[posmuj + 1:posmuj + 4].strip()
            elif posmuj == -1:
                user['sexo'] = line[posvar + 1:posvar + 4].strip()

            if posdist1 == -1:
                if posdist2 == -1:
                    user['direccion'] = line[posguion + 6:posdist3].strip()
                    user['circunscripcion'] = line[posdist3:posdist3 + largodist3].strip()
                    user['mesa'] = line[posdist3 + largodist3:cierremesa].strip()
                elif posdist3 == -1:
                    user['direccion'] = line[posguion + 6:posdist2].strip()
                    user['circunscripcion'] = line[posdist2:posdist2 + largodist2].strip()
                    user['mesa'] = line[posdist2 + largodist2:cierremesa].strip()
            else:
                user['direccion'] = line[posguion + 6:posdist1].strip()
                user['circunscripcion'] = line[posdist1:posdist1 + largodist1].strip()
                user['mesa'] = line[posdist1 + largodist1:cierremesa].strip()

            users.append(user)

for user in users:
    OutputFile.write(user['nombre'] + ';' + user['rut'] + ';' +user['sexo'] + ';' + user['direccion'] + ';' + user['circunscripcion'] + ';' + user['mesa'])
    OutputFile.write("\n")
rawdata.close()
OutputFile.close()
