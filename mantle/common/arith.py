from mantle import DefineAdd, DefineSub, DefineNegate, DefineASR

def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin=cin, cout=cout)(**kwargs)

def Sub(n, cin=False, cout=False, **kwargs):
    return DefineSub(n, cin=cin, cout=cout)(**kwargs)

def Negate(width, **kwargs):
    return DefineNegate(width)(**kwargs)

def ASR(width, **kwargs):
    return DefineASR(width)(**kwargs)
