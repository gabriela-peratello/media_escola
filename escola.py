def verificar_media(media:int|float) -> str:
    """Essa função tem como objetivo retornar se o aluno passou ou não de ano"""
    
    if media >=7:
        return "Aprovado"
    elif media < 5:
        return "Reprovado"
    else:
        return "Recuperação"


if __name__ == "__main__":
    print(verificar_media(3))