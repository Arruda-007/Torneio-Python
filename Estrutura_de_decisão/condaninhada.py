# : sera 
usuario_ativo = False
nivel_acesso = 5

if usuario_ativo:
    if nivel_acesso >= 3:
        print('Acesso adm')
    else:
        print('Acesso de Usuario Padrao')
else:
    print('Conta desativada')

#CORRETO