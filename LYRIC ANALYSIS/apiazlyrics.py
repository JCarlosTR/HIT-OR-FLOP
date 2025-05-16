import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd
import unicodedata
import time
import random
import os

def descargar_letra(autor,cancion):
    url = f"https://www.azlyrics.com/lyrics/{autor}/{cancion}.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    
    for element in soup.find_all(string=lambda text: isinstance(text, Comment)):
        if "Usage of azlyrics.com" in element:
            lyrics = ""
            for sibling in element.next_siblings:
                if isinstance(sibling, Comment) and "MxM banner" in sibling:
                    break
                if isinstance(sibling, str):
                    sibling = convert_to_ascii(sibling)
                    lyrics += sibling.strip() + "\n"
            break
        
    lyrics = lyrics.strip()
    return lyrics

def convert_to_ascii(text):
    if isinstance(text, str):
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text)
            if not unicodedata.combining(c)
        )
    return text

def comprobar(nombre,titulo):
    
    if nombre == "cardib":
        nombre = "cardi-b"
    
    elif nombre == "bts":
        nombre = "bangtanboys"
        
    elif nombre == "pinksweat$":
        nombre = "pinksweats"
        
    elif nombre == "børns":
        nombre = "borns"
        
    elif nombre == "ac/dc":
        nombre = "acdc"
        
    elif nombre == "j.cole":
        nombre = "jcole"
        
    elif nombre == "beyonce":
        nombre = "beyonceknowles"
        
    elif nombre == "elleyduhe":
        nombre = "elleyduh"
        
    elif nombre == "ghost":
        nombre = "ghostbc"
        
    elif nombre == "jhayco":
        nombre = "jhaycortez"
        
    elif nombre == "maneskin":
        nombre = "mneskin"
        
    elif nombre == "bachmanturneroverdrive":
        nombre = "btobachmanturneroverdrive"
        
    elif nombre == "panicatdisco":
        nombre = "panicatthedisco"
        
    if titulo == "undia":
        titulo = "undiaoneday"
    
    elif titulo == "dreams2004remaster":
        titulo = "dreams"
        
    elif titulo == "ily":
        titulo = "ilyiloveyoubaby"
    
    elif titulo == "tattooremixwithcamilo":
        titulo = "tattooremix"
        
    elif titulo == "christmasmustbetonightremastered2001":
        titulo = "christmasmustbetonight"
    
    elif titulo == "sunflowerspidermanintothespiderverse":
        titulo = "sunflower"
    
    elif titulo == "sensaciondelbloque":
        titulo = "sensacindelbloque"
    
    elif titulo == "imgood":
        titulo = "imgoodblue"
    
    elif titulo == "quevedobzrpmusicsessionsvol52":
        titulo = "quevedobzrpmusicsessions52"
    
    elif titulo == "starwalkin":
        titulo = "starwalkinleagueoflegendsworldsanthem"
        
    elif titulo == "betty":
        titulo = "bettygetmoney"
        
    elif titulo == "revenge":
        titulo = "revenge566988"
        
    elif titulo == "mrbrightside":
        titulo = "mrbrightside39068"
    
    elif titulo == "yettocome":
        titulo = "yettocomethemostbeautifulmoment"
        
    elif titulo == "hotelcalifornia2013remaster":
        titulo = "hotelcalifornia"
        
    elif titulo == "nosiguemodasakaellanosiguemodas":
        titulo = "nosiguemodas"
        
    elif titulo == "gentleonmymindremastered2001":
        titulo = "gentleonmymind"
        
    elif titulo == "tequieropa mi":
        titulo = "tequieropami"
        
    elif titulo == "merehuso":
        titulo = "merehso"
        
    elif titulo == "whenyoureinlovewithabeautifulwomanremastered1996":
        titulo = "whenyoureinlovewithabeautifulwoman"
        
    elif titulo == "sharpdressedman2003remaster":
        titulo = "sharpdressedman"
        
    elif titulo == "lastfridaynight":
        titulo = "lastfridaynighttgif"
        
    elif titulo == "quizasremix":
        titulo = "quizs"
        
    elif titulo == "permitame":
        titulo = "permtame"
        
    elif titulo == "tattooukpopmix":
        titulo = "tattoo"
        
    elif titulo == "cuandotebese":
        titulo = "cuandotebes"
    
    return nombre, titulo

def prearreglo_artista(c):
    lista = []
    
    kk = c.split(" ")
    for bich in kk:
        if bich == "the":
            pass
        else:
            lista.append(bich)
            
    o = " ".join(lista)
    return o

def arreglar_cadena(c):
    
    letra = list(c)
    parentesis_abierto = None
    no = []
    
    for i,elem in enumerate(letra):
        if elem == "(":
            parentesis_abierto = letra.index(elem)
            break
        if elem in quitar:
            no.append(i)
            
    c = "".join(letra)
    
    if parentesis_abierto is not None:
        c = c[:parentesis_abierto].strip()
        
    letra_2 = list(c)
    titulo_real=[]
    for i,caracter in enumerate(letra_2):
        if i not in no:
            titulo_real.append(caracter)
        
    c = "".join(titulo_real)
    
    return c

dic = {}

df = pd.read_csv("C:/Users/josep/Downloads/data_by_popular_inversed_Mar25.csv")
#df = pd.read_csv("C:/Users/Jose/Downloads/Zona proyecto/data_by_popular_Mar25.csv")
#df = pd.read_csv("C:/Users/laura/Downloads/Popular/data_by_popular.csv")

bs = 10
ini,fin = 0,19999

for start in range(ini,fin,bs):
    batch = df.iloc[start:start+bs]

    for _, row in batch.iterrows():
        artistas = []
        prueba = str(row["artist_name"])
        prueba2 = prueba[0:len(prueba)].split(";")
        
        for artista in prueba2:
            juan = "".join(artista.lower())
            artistas.append(juan)
        tup_artistas = tuple(artistas)
            
        titulo = "".join(str(row["track_name"]).lower())
            
        dic[titulo] = tup_artistas


quitar = [",","!","¡","?","¿",".",":",";","'","´","+","-","&","$","<","’","/"]
contador,recontador = 0,0

lista = []

with open("unpopus_Mar2025.txt","a") as f:
    for v,k in dic.items():
        if contador < 200:
            try:
                
                print(k[0])
                
                prenombre = prearreglo_artista(k[0])
                
                nombre = "".join(str(prenombre).strip()[0:len(prenombre)].split())
                titulo = "".join(str(v).split())
                print(nombre,titulo)
                
                nombre = convert_to_ascii(nombre)
                titulo = convert_to_ascii(titulo)            
                
                nombre = arreglar_cadena(nombre)
                titulo = arreglar_cadena(titulo)
                
                nombre,titulo = comprobar(nombre,titulo)    
                
                print(nombre,titulo)
                escribir = descargar_letra(nombre,titulo)
                f.write(escribir)
                f.write("\n---------------------------------------------------\n")
                
                contador += 1
                
                time.sleep(random.uniform(15,30))
                
                print(contador,recontador)
                
                lista.append((k[0],v))
                
            except UnicodeEncodeError:
                print("Exploto por Unicode")
                recontador += 1
                print(contador, recontador)
                pass
            
            except requests.exceptions.HTTPError:
                try:
                    
                    prenombre = prearreglo_artista(k[1])
                    
                    nombre = "".join(str(prenombre).strip()[0:len(prenombre)].split())
                    nombre = convert_to_ascii(nombre)
                    nombre = arreglar_cadena(nombre)
                    
                    nombre,titulo = comprobar(nombre,titulo)
                        
                    print(nombre,titulo)
                    escribir = descargar_letra(nombre,titulo)
                    f.write(escribir)
                    f.write("\n---------------------------------------------------\n")
                    
                    contador += 1
                    
                    time.sleep(random.uniform(15,30))
                    
                    print(contador,recontador)
                    
                    lista.append((k[1],v))
                    
                except requests.exceptions.HTTPError:
                    recontador += 1
                    print(contador, recontador)
                    pass
                
                except KeyError:
                    recontador += 1
                    print(contador, recontador)
                    pass
                
                except IndexError:
                    recontador += 1
                    print(contador, recontador)
                    pass
                
                except Exception:
                    pass
        else:
            break


archivo_csv = "artist_cancion_unpop_Mar2025.csv"

# Verificar si el archivo ya existe
if os.path.exists(archivo_csv):
    df2_existente = pd.read_csv(archivo_csv)
    df2_nuevo = pd.DataFrame(lista, columns=["artista", "nombre_cancion"])
    df2 = pd.concat([df2_existente, df2_nuevo], ignore_index=True)
else:
    df2 = pd.DataFrame(lista, columns=["artista", "nombre_cancion"])

df2.to_csv(archivo_csv, index=False)

        
        
            
