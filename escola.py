def verificar_media(media:int|float) -> str:
    """Essa função tem como objetivo retornar se o aluno passou ou não de ano"""

    # Testando para ver se a média é um número
    if not isinstance(media, int):
        raise TypeError ("Tipo inválido, a entrada deve ser numérica.")

    if media >=7: 
        return "Aprovado"
    elif media <= 4: 
        return "Reprovado"
    else: 
        return "Recuperação"
    


if __name__ == "__main__":
    print(verificar_media(6))