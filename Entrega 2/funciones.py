def generarEstructura(names,goals,goals_avoided,assists):
    nombres= list(name.strip()for name in names.split(","))
    valores= list(zip(goals,goals_avoided,assists))
    return dict(zip(nombres,valores))

def goleadorEs(info):
    claveMax = max(info, key=lambda x: info[x][0])
    goles=info[claveMax][0]
    print("El goleador es", claveMax," con ",goles," goles.")
    return {claveMax:goles}

def masInfluyente(info):
    masInflu=[tuple([nombre,sum([dato[0]*1.5,dato[1]*1.25,dato[2]*1])])
                    for nombre,dato in info.items()]
    print(max(masInflu, key=lambda x: x[1]))

def promedioGolesGeneral(info):
    goles=0
    for clave in info:
        goles+=info[clave][0]
    print(f"promedio de goles de equipo durante la temporada fue de {goles/25}")

def promedioGolesGoleador(goleador):
    clave=next(iter(goleador.keys()))
    print(f"promedio de goles del goleador {clave} durante la termporada fue de {goleador[clave]/25}")