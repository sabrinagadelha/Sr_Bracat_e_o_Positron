import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

h_cortado = 1.0545718e-34
massa_eletron = 9.1093837e-31
n1 = 1
n2 = 2
L = 1
times = np.linspace(0, 20, 21)
fig, ax = plt.subplots(figsize=(8,5))
line, = ax.plot([],[])

#ideias para o poço de potencial finito: 
#   i) o que plotar: niveis de energia, função de onda e densidade de probabilidade
#   ii) usuário deve escolher números diferentes de n e observar as diferenças
#   iii) usuário deve brincar com as unidades de L, indo de nm a um
#   iv) evolução temporal

def poço_infinito(largura, numero_quantico):
    fig, (wave_f, prob) = plt.subplots(1,2, figsize=(18,7), sharey=True)
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
    fig.savefig('imagem.png')
    plt.legend(fontsize=19)

def evoluc_temp_pç_finito(frame):
    x = np.linspace(0,L,200)
    wave1 = np.sqrt(2/L)*np.sin(n1*np.pi*x/L)
    wave2 = np.sqrt(2/L)*np.sin(n2*np.pi*x/L)
    e1 = (n1*np.pi*h_cortado/L)**2*1/(2*massa_eletron)
    e2 = (n2*np.pi*h_cortado/L)**2*1/(2*massa_eletron)
    c = 1/(np.sqrt(2))
    t = times[frame]
    psi = (c*np.exp(-1j*e1*t/h_cortado)*wave1 + c*np.exp(-1j*e2*t/h_cortado)*wave2)
    prob_t = (abs(psi))**2
    line.set_data(x, prob_t)
    return line

ani = FuncAnimation(fig, evoluc_temp_pç_finito, frames=21, interval=50, blit=False)
ani.save("animac_teste.gif", writer='pillow', fps=21, dpi=100)
plt.close(fig)
print(times[0])