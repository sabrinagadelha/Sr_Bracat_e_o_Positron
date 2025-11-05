import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

h_cortado = 1.0545718e-34
massa_eletron = 9.1093837e-31
times = np.linspace(0, 20, 200) 

fig, ax = plt.subplots(figsize=(8,5))

def poço_infinito(largura, numero_quantico):
    figura, (wave_f, prob) = plt.subplots(1,2, figsize=(18,7), sharey=True)
    x_wave_func = np.linspace(0, largura, 200)
    y_wave_func = np.sqrt(2/largura)*np.sin(numero_quantico*np.pi*x_wave_func/largura)
    wave_f.plot(x_wave_func, y_wave_func, color='pink')
    wave_f.set_xlabel('x', fontsize = 20, color = 'black')
    wave_f.set_title('$\phi_x$: função de onda', fontsize = 24)
    wave_f.tick_params(direction='inout', length=15, width=2, labelsize=16)
    wave_f.grid(color='green', alpha=0.2)
    x_prob = np.linspace(0, largura, 2000)
    y_prob = 2/largura*(np.sin(numero_quantico*np.pi*x_prob/largura))**2
    prob.plot(x_prob, y_prob, color='purple')
    prob.set_xlabel('x', fontsize = 20, color = 'black')
    prob.set_title('$|\phi_x|^2$: densidade de probabilidade', fontsize = 24)
    prob.tick_params(direction='inout', length=15, width=2, labelsize=16)
    prob.grid(color='green', alpha=0.2)
    figura.savefig('imagem.png')
    #plt.legend(fontsize=19)

def evoluc_temp_pç_finito(frame, L, n1, n2):
    max_amplitude_square = (np.sqrt(2/L) * (1/np.sqrt(2) + 1/np.sqrt(2)))**2
    ax.set_ylim(0, max_amplitude_square * 1.1) 
    ax.set_xlim(0, L)
    x = np.linspace(0,L,200)

    wave1 = np.sqrt(2/L)*np.sin(n1*np.pi*x/L)
    wave2 = np.sqrt(2/L)*np.sin(n2*np.pi*x/L) 
    
    e1 = (np.pi*h_cortado/L)**2 * n1**2 / (2*massa_eletron)
    e2 = (np.pi*h_cortado/L)**2 * n2**2 / (2*massa_eletron)
    
    c = 1/(np.sqrt(2))
    c1 = 1/np.sqrt(100)
    c2 = np.sqrt(99/100)
    t = times[frame]
    t *= 300
    
    psi = (c *wave1* np.exp(-1j*e1*t/h_cortado) + 
           c *wave2* np.exp(-1j*e2*t/h_cortado))
    
    prob_t = (np.abs(psi))**2 

    delta_x = x[1] - x[0]
    valor_esperado_x = np.sum(prob_t*x*delta_x)
    nome = f'frames_gif/frame{frame:03d}'
    
    #line.set_data(x, prob_t)
    ax.plot(x, prob_t, color='pink', linewidth=2, zorder=3, label='$|\phi|(t, x)^2$')
    ax.plot(x, abs(wave1)**2, alpha=0.25, color='blue', linestyle='--', zorder=1, label='$|\phi_1(0, x)|^2$')
    ax.plot(x, abs(wave2)**2, alpha=0.25, color='green', linestyle='--', zorder=2, label='$|\phi_2(0, x)|^2$')
    ax.axvline(valor_esperado_x, color='purple', linestyle='--', linewidth=2, zorder=4, label='$<x>$')
    ax.set_xlabel('x', fontsize = 20, color = 'black')
    ax.set_title('$|\phi_x|^2$: densidade de probabilidade', fontsize = 24)
    ax.tick_params(direction='inout', length=15, width=2, labelsize=16)
    ax.grid(color='green', alpha=0.2)
    ax.set_title(f'Tempo: {t:.2f} s', fontsize=12) 
    ax.legend(fontsize=10)
    fig.savefig(nome)
    #plt.pause(0.00001)
    ax.clear()


#ani = FuncAnimation(fig, evoluc_temp_pç_finito, frames=len(times), interval=50, blit=True)
#ani.save("animac_teste.gif", writer='pillow', fps=20, dpi=100) # Mudei fps para 20


print("-----------------------------------------------------------------")
print('Vamos inicar a simulação de poço quadrado infinito! Para isso, vamos começar estudando os efeitos da escolha do número quântico')
print('Veja como se comportam a função de onda e a densidade de probabilidade para um elétron confinado no estado fundamental')
print('Obs: para visualizar imagens estáticas, acesse o arquivo imagem.png')

poço_infinito(1,1)

print('Observe a quantidade de ventres da função: apenas 1. Esse número está diretamente ligada com o número quântico, ou seja, o número que indica o nível ocupado pela partícula no poço.')
print('O nível fundamental é correspondente ao número quântico n=1. Vamos ver como fica o primeiro nível excitado: n=2.')
flag = input('Para continuar, digite: "s": ')

if(flag=='s'):
    poço_infinito(1,2)
print('Observe que agora temos 2 ventres, correspondendo a n=2!')
print('Explore o simulador inserindo números e observando o resultado. Quando quiser passar para a próxima etapa, digite o número 0')

numero_1 = int(input('Insira um número quântico: '))
while(numero_1!=0):
    poço_infinito(1,numero_1)
    numero_1 = int(input('Insira um número quântico: '))

print('Agora vamos explorar um pouco a ação da mudança no comprimento do poço! Aqui vamos fixar n=2. Já olhamos o gráfico de n=2 e L=1, mas não custa relembrar como ele se comporta.')
poço_infinito(1,2)
flag='n'
flag=input('Para continuar, digite "s": ')
print('Subindo L para 10, a relação entre a função de onda e a densidade de probabilidade muda. Isso acontece porque a densidade de probabilidade é normalizada: a probabilidade de encontrar a partícula em algum lugar do espaço é sempre igual a 1. Assim, como a base da forma de onda aumenta com L aumentando, a amplitude deve diminuir, para manter a integral igual a 1')
poço_infinito(10,2)
flag = input('Para continuar, digite "s": ')
poço_infinito(100,2)
print('Aqui L vale 100 e podemos ver como a densidade de probabilidade começa a se tornar mais uniforme')

print('Explore o simulador inserindo números e observando o resultado. Lembre-se de usar ponto . como separador decimal. Quando quiser passar para a próxima etapa, digite o número 0')
numero_2 = float(input('Insira um valor para L: '))
while(numero_2!=0):
    poço_infinito(numero_2, 2)
    numero_2 = float(input('Insira um valor para L: '))

print('Por último, vamos explorar o efeito da evolução temporal de estados em superposição. Começando com o caso de superposição entre os estados com n_1 = 1 e n_2 = 2, podemos observar o comportamento representado no arquivo evolucao.gif.')

for i in range(120):
    evoluc_temp_pç_finito(i, 1, 1, 2)
plt.close(fig) # Agora é seguro fechar
file_list = sorted(glob.glob('frames_gif/*.png'))
if not file_list: 
    print('nenhum arquivo de imagem encontrado')
else:
    img_principal = Image.open(file_list[0])
    frames = [Image.open(file) for file in file_list[1:]]
    img_principal.save(
        'evolucao.gif',
        format='GIF',
        append_images=frames,
        save_all=True,
        duration=50,
        loop=0
    ) 

print('Agora é a sua vez!')
n1, n2 = input('Insira dois números, referentes ao primeiro número quântico e ao segundo separando-os por um espaço: ').split()
n1 = int(n1)
n2 = int(n2)
while(n1!=0):
    for i in range(120):
        evoluc_temp_pç_finito(i, 1, n1, n2)
    plt.close(fig) 
    file_list = sorted(glob.glob('frames_gif/*.png'))
    if not file_list: 
        print('nenhum arquivo de imagem encontrado')
    else:
        img_principal = Image.open(file_list[0])
        frames = [Image.open(file) for file in file_list[1:]]
        img_principal.save(
            'evolucao.gif',
            format='GIF',
            append_images=frames,
            save_all=True,
            duration=50,
            loop=0
        ) 
    n1, n2 = input('Insira dois números, referentes ao primeiro número quântico e ao segundo separando-os por um espaço: ').split()
    n1 = int(n1)
    n2 = int(n2)
