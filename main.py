import os
import discord
#import sys
from discord.ext import commands
from discord import DMChannel
from dotenv import load_dotenv
#from datetime import datetime
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('token')

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

#variables globales
globalUsuario = "null"

bot = commands.Bot(command_prefix="/")


@bot.command(name='info')
async def info(ctx, user: discord.Member, *, mensaje=None):
    global globalUsuario
    globalUsuario = user.name
    mensaje = "Hola! Soy Bibibot. Te doy la info basica sobre subir tu cuenta de Pokemon GO con la ayuda de Andybot. Obviamente, esto tiene un costo."
    embed = discord.Embed(
        title=mensaje,
        description='Antes, necesito que conoscas las reglas.',
        color=0x0000ff)
    embed.set_author(name="El Bibibot de Andybot",
                     url="https://linktr.ee/Andybot",
                     icon_url="")
    #embed.set_thumbnail(url="")
    embed.add_field(name="Digita el comando /reglas",
                    value='Y comenzamos...',
                    inline=True)
    await user.send(embed=embed)
    print("Bot iniciado para: " + globalUsuario)


##@bot.command(name='dm')
##async def dm(ctx):
##	await ctx.sendDM('Hola')


@bot.command(name='reglas')
async def reglas(ctx):
    await ctx.send("***REGLAS***")
    await ctx.send('1.- Andy necesita tener libertad para uso de polvos y MTs')
    await ctx.send(
        '2.- Si Andy pide un poke, hay que intentar conseguirlo, no necesariamente rank 1 pero si cercano a 0/15/15 en los casos que correspondan, y maximo con 5 de ataque'
    )
    await ctx.send(
        '3.- Si quieres que Andy juegue durante Liga Ultra necesitas Drapion XL y/o Politoed XL y algun que otro poke para la ultra'
    )
    await ctx.send(
        '4.- Si nos encontramos en el ultimo mes de la temporada, la regla 3 es obligatoria.'
    )
    await ctx.send(
        '5.- No hay horario exacto de juego, Andy te avisara cuando entre para que dejes libre tu cuenta, esperando que no tengas activado incienso, mega o algo parecido'
    )
    await ctx.send(
        '6.- Necesitamos tu participacion en los torneos de colaboradores, para convivir y divertirse, ya que Andy no solo quiere ayudarlos a conseguir su leyenda, sino que tambien ustedes lo logren algun dia'
    )

    await ctx.send(
        '*NOTA: No aplica el softban porque Andy no captura pokes del mapa, solo de GBL y esos no cuentan como softban :D*'
    )
    await ctx.send(
        '*NOTA: La subida a leyenda no se da en 2, 3 o 4 semanas desde que le das tu cuenta a Andy, sino durante el transcurso de la temporada, por lo que se agradece bastante la paciencia*'
    )

    await ctx.send(
        'Si estas de acuerdo con seguir estas reglas, por favor, digita: /si')


@bot.command(name='si')
async def si_reglas(ctx):
    #await ctx.send("Perfecto. Por quedar poco tiempo para terminar la temporada, se estan recibiendo solo cuentas con elo mayor a 2500.")
    #await ctx.send("Perfecto. Por quedar pocos dias para terminar la temporada, se estan recibiendo solo cuentas con elo mayor a 2750.")
    #await ctx.send('Si tu rango actual es experto con mas de 2750 puntos por favor digita: /rango experto')
    await ctx.send(
        'Perfecto! Ahora necesito saber tu rango actual. Usa el comando "/rango experto" si tienes elo > 2750 o "/rango veterano" si tienes elo >2500 o "/rango ace" si tienes elo > 2000 o "/rango 20" si estas en rango 20 o menor'
    )


@bot.command(name='rango')
async def rango(ctx):
    idRango = ctx.message.content[7:]
    if (idRango == '20'):
        costo = 100
    elif (idRango == 'ace'):
        costo = 60
    elif (idRango == 'veterano'):
        costo = 50
    elif (idRango == 'experto'):
        costo = 30
    else:
        await ctx.send(
            "Lo siento, no pude reconocer el rango escrito. Intentalo nuevamente. Ejemplo: /rango ace"
        )
        return

    await ctx.send("El costo del servicio es de: " + str(costo) +
                   " USD. (dolares estadounidenses)")
    #await ctx.send("*NOTA: El actual costo es debido a que quedan pocos dias para que termine la actual temporada. Si nos buscas a inicios de temporada, los costos son mas bajos.*")
    await ctx.send(
        "Para conocer los metodos de pago y seguir con la informacion, digita: /pago"
    )


@bot.command(name='pago')
async def pago(ctx):
    await ctx.send(
        "*NOTA: el pago lo realizaras luego de conversar y definir detalles con Andybot. Por ahora solo necesito saber que metodo podrias usar.*"
    )
    await ctx.send(
        "---------------------------------------------------------------------------"
    )
    await ctx.send("Metodo 1: Transferencia Bancaria (Valido solo para Mexico)"
                   )
    await ctx.send("Santander")
    await ctx.send("5579 1003 3996 8024")
    await ctx.send(
        "Metodo 2: Western Union: Andrea Rubi Bravo Solis (Valido Internacionalmente)"
    )
    await ctx.send(
        "Metodo 3: Paypal: andrea.bravo@outlook.es (Valido Internacionalmente)"
    )
    await ctx.send(
        "---------------------------------------------------------------------------"
    )
    await ctx.send(
        "Para continuar, elije el metodo de pago que usaras luego de hablar con Andy. Digita: /metodo 1, /metodo 2 o /metodo 3."
    )


@bot.command(name='metodo')
async def metodo(ctx):
    metodoElegido = ""  #Variable no tan necesaria por ahora, pero posiblemente si a futuro.
    metodo = ctx.message.content[8:]
    if (metodo == '1'):
        metodoElegido = "Transferencia"
    elif (metodo == '2'):
        metodoElegido = "Western Union"
    elif (metodo == '3'):
        metodoElegido = "Paypal"
    else:
        await ctx.send(
            "Lo siento, no pude reconocer el metodo escrito. Intentalo nuevamente. Ejemplo: /metodo 2"
        )
        return

    await ctx.send(
        "Si deseas continuar con el servicio, conversa con Andybot mediante este link: https://wa.me/5219211035109"
    )
    await ctx.send(
        "Y enviale el siguiente mensaje, ingresando los datos que te he dado:")
    await ctx.send(
        "Estimada Andybot, converse con tu Bibibot. Sobre el servicio de subir cuentas, acepto las reglas, mi rango actual es <ingresa rango>, acepto el costo de <ingresa costo> dolares y el pago lo realizare mediante "
        + metodoElegido +
        ". Espero tu respuesta para refinar detalles. Saluditos.")
    await ctx.send(
        "-----------------------------------------------------------------------------------"
    )
    await ctx.send(
        "Es todo de parte de Bibibot! :D Gracias por comunicarte conmigo :3 Exitos!"
    )

    #Para cuando se necesite un log de todos los que aceptan el servicio.
    #now = datetime.now()
    #momento = str(now.year) + "-"+ str(now.month) + "-" + str(now.day) + " " +  str(now.hour) + ":" + str(now.minute)
    #print(globalUsuario + " / " + globalRango + " / " + globalCosto + " / " + metodoElegido + " / " + momento)


@bot.command(name='prueba', pass_context=True)
async def prueba(ctx):
    user = ctx.author.send()
    await DMChannel.send(user, "Put the message here")


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Necesito que te etiquetes. Ejemplo: /info @Bibibot")

    if isinstance(error, commands.MemberNotFound):
        print("ERROR: MemberNotFound. Info no enviada al usuario: " +
              ctx.message.content[6:])


#@rango.error
#async def rango_error(ctx, error):
#if isinstance(error, commands.CommandNotFound):
#await ctx.send("Lo siento, no pude reconocer el rango escrito. intentalo nuevamente. Ejemplo: /rango ace")

#@metodo.error
#async def metodo_error(ctx, error):
#if isinstance(error, commands.CommandNotFound):
#await ctx.send("Lo siento, no pude reconocer el metodo escrito. Intentalo nuevamente. Ejemplo: /metodo 2")

keep_alive()

#bloque try añadido para intentar mantener siempre activo el bot, anteriormente solo se usaba el bot.run(TOKEN)
try:
    bot.run(TOKEN)
except:
    os.system("kill 1")
#bot.run(TOKEN)