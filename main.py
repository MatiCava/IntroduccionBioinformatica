listCondH = ['Glu', 'Ala', 'Leu', 'met', 'Gln Lys', 'Arg', 'His']
listCondB = ['Val', 'Ile', 'Tyr', 'Cys', 'Trp', 'Phe', 'Thr']


def clasificar(proteina):
    result = []
    for aminoacido in proteina:
        if aminoacido in listCondH:
            result.append('H')
        elif aminoacido in listCondB:
            result.append('B')
        else:
            result.append('L')
    return result
