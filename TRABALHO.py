n = int(input())
s1 = str(input())
s2 = str(input())
f = str(input())
p = 0
resultado = ''
result1 = ''

# testando se é possível

if len(s1) != len(s2):
    print('ERRO')
    p = 1
if p == 0:
    for a in range(n):
        if (s1[a] == '0' or s1[a] == '1') and (s2[a] == '0' or s2[a] == '1'):
            continue
        else:
            print('ERRO')
            p = 1

# Realizando as operações


# Se for calculo simples:

if p == 0:
    if len(f.split()) == 3:
        if f.split()[1] == 'AND':  # AND  # teste para saber qual operação fazer
            for b in range(n):
                if s1[b] == s2[b]:
                    resultado += '1'
                else:
                    resultado += '0'
        elif f.split()[1] == 'OR':  # OR
            for b in range(n):
                if s1[b] == '1' or s2[b] == '1':
                    resultado += '1'
                else:
                    resultado += '0'
        elif f.split()[1] == 'XOR':  # XOR
            for b in range(n):
                if s1[b] != s2[b]:
                    resultado += '1'
                else:
                    resultado += '0'
        elif f.split()[1] == 'NAND':  # NAND
            for b in range(n):
                if s1[b] == s2[b]:
                    resultado += '0'
                else:
                    resultado += '1'
        elif f.split()[1] == 'NOR':  # NOR
            for b in range(n):
                if s1[b] == '1' or s2[b] == '1':
                    resultado += '0'
                else:
                    resultado += '1'
        elif f.split()[1] == 'MOR':
            if f.split()[0] == 'S1' and f.split()[2] == 'S2':  # MOR  # Teste para ordem, pois no MOR importa.
                naoA = ''
                for b in range(n):
                    if s1[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s2[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
            if f.split()[0] == 'S1' and f.split()[2] == 'S1':  # Teste para ordem, pois no MOR importa.
                naoA = ''
                for b in range(n):
                    if s1[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s1[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
            if f.split()[0] == 'S2' and f.split()[2] == 'S1':  # Teste para ordem, pois no MOR importa.
                naoA = ''
                for b in range(n):
                    if s2[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s1[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
            if f.split()[0] == 'S2' and f.split()[2] == 'S2':  # Teste para ordem, pois no MOR importa.
                naoA = ''
                for b in range(n):
                    if s2[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s2[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
        print(resultado)

    # Se for calculo composto:

    if len(f.split()) == 5:
        if f.split()[1] == 'AND':  # AND  # Teste para saber qual calculo fazer primeiro e realizar
            for b in range(n):
                if s1[b] == s2[b]:
                    resultado += '1'
                else:
                    resultado += '0'
            if f.split()[3] == 'AND':  # AND Secundario  # Teste para saber o segundo calculo e realizar
                if f.split()[4] == 'S2':  # Teste pois a ordem importa
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'OR':  # OR Secundario
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'XOR':  # XOR Secundario
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] != s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] != s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'NAND':  # NAND Secundario
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'NOR':  # NOR Secundario
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'MOR':  # MOR Secundario
                if f.split()[4] == 'S2':  # Aqui temos apenas 2 opçoes apenas
                    naoA = ''
                    for b in range(n):
                        if resultado[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                if f.split()[4] == 'S1':
                    naoA = ''
                    for b in range(n):
                        if s1[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
        #
        elif f.split()[1] == 'OR':  # OR
            for b in range(n):
                if s1[b] == '1' or s2[b] == '1':
                    resultado += '1'
                else:
                    resultado += '0'
            if f.split()[3] == 'AND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'OR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'XOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] != s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] != s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'NAND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'NOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'MOR':
                if f.split()[4] == 'S2':
                    naoA = ''
                    for b in range(n):
                        if resultado[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                if f.split()[4] == 'S1':
                    naoA = ''
                    for b in range(n):
                        if s1[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
        #
        elif f.split()[1] == 'XOR':
            for b in range(n):
                if s1[b] != s2[b]:
                    resultado += '1'
                else:
                    resultado += '0'
            if f.split()[3] == 'AND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'OR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'XOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] != s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] != s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'NAND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'NOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'MOR':
                if f.split()[4] == 'S2':
                    naoA = ''
                    for b in range(n):
                        if resultado[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                if f.split()[4] == 'S1':
                    naoA = ''
                    for b in range(n):
                        if s1[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
        #
        elif f.split()[1] == 'NAND':
            for b in range(n):
                if s1[b] == s2[b]:
                    resultado += '0'
                else:
                    resultado += '1'
            if f.split()[3] == 'AND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'OR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'XOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] != s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] != s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'NAND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'NOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'MOR':
                if f.split()[4] == 'S2':
                    naoA = ''
                    for b in range(n):
                        if resultado[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                if f.split()[4] == 'S1':
                    naoA = ''
                    for b in range(n):
                        if s1[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
        #
        elif f.split()[1] == 'NOR':
            for b in range(n):
                if s1[b] == '1' or s2[b] == '1':
                    resultado += '0'
                else:
                    resultado += '1'
            if f.split()[3] == 'AND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'OR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'XOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] != s2[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
                elif f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] != s1[b]:
                            result1 += '1'
                        else:
                            result1 += '0'
            elif f.split()[3] == 'NAND':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == s2[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == s1[b]:
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'NOR':
                if f.split()[4] == 'S2':
                    for b in range(n):
                        if resultado[b] == '1' or s2[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
                if f.split()[4] == 'S1':
                    for b in range(n):
                        if resultado[b] == '1' or s1[b] == '1':
                            result1 += '0'
                        else:
                            result1 += '1'
            elif f.split()[3] == 'MOR':
                if f.split()[4] == 'S2':
                    naoA = ''
                    for b in range(n):
                        if resultado[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s2[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
                if f.split()[4] == 'S1':
                    naoA = ''
                    for b in range(n):
                        if s1[b] == '1':
                            naoA += '0'
                        else:
                            naoA += '1'
                    for b in range(n):
                        if naoA[b] == '1' or s1[b] == '1':
                            result1 += '1'
                        else:
                            result1 += '0'
        #
        elif f.split()[1] == 'MOR':
            if f.split()[0] == 'S1' and f.split()[2] == 'S2':
                naoA = ''
                for b in range(n):
                    if s1[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s2[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
                if f.split()[3] == 'AND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'OR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'XOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] != s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] != s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'NAND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'NOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'MOR':
                    if f.split()[4] == 'S2':
                        naoA = ''
                        for b in range(n):
                            if resultado[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    if f.split()[4] == 'S1':
                        naoA = ''
                        for b in range(n):
                            if s1[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
            if f.split()[0] == 'S1' and f.split()[2] == 'S1':
                naoA = ''
                for b in range(n):
                    if s1[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s1[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
                if f.split()[3] == 'AND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'OR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'XOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] != s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] != s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'NAND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'NOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'MOR':
                    if f.split()[4] == 'S2':
                        naoA = ''
                        for b in range(n):
                            if resultado[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    if f.split()[4] == 'S1':
                        naoA = ''
                        for b in range(n):
                            if s1[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
            if f.split()[0] == 'S2' and f.split()[2] == 'S1':
                naoA = ''
                for b in range(n):
                    if s2[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s1[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
                if f.split()[3] == 'AND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'OR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'XOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] != s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] != s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'NAND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'NOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'MOR':
                    if f.split()[4] == 'S2':
                        naoA = ''
                        for b in range(n):
                            if resultado[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    if f.split()[4] == 'S1':
                        naoA = ''
                        for b in range(n):
                            if s1[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
            if f.split()[0] == 'S2' and f.split()[2] == 'S2':
                naoA = ''
                for b in range(n):
                    if s2[b] == '1':
                        naoA += '0'
                    else:
                        naoA += '1'
                for b in range(n):
                    if naoA[b] == '1' or s2[b] == '1':
                        resultado += '1'
                    else:
                        resultado += '0'
                if f.split()[3] == 'AND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'OR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'XOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] != s2[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                    elif f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] != s1[b]:
                                result1 += '1'
                            else:
                                result1 += '0'
                elif f.split()[3] == 'NAND':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == s2[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == s1[b]:
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'NOR':
                    if f.split()[4] == 'S2':
                        for b in range(n):
                            if resultado[b] == '1' or s2[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                    if f.split()[4] == 'S1':
                        for b in range(n):
                            if resultado[b] == '1' or s1[b] == '1':
                                result1 += '0'
                            else:
                                result1 += '1'
                elif f.split()[3] == 'MOR':
                    if f.split()[4] == 'S2':
                        naoA = ''
                        for b in range(n):
                            if resultado[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s2[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
                    if f.split()[4] == 'S1':
                        naoA = ''
                        for b in range(n):
                            if s1[b] == '1':
                                naoA += '0'
                            else:
                                naoA += '1'
                        for b in range(n):
                            if naoA[b] == '1' or s1[b] == '1':
                                result1 += '1'
                            else:
                                result1 += '0'
        print(result1)
