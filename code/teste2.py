import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob

h_cortado = 1.0545718e-34
massa_eletron = 9.1093837e-31
#n1 = 1
#n2 = 2
#L = 1
times = np.linspace(0, 20, 200) 

fig, ax = plt.subplots(figsize=(8,5))
# A linha que será atualizada
#line, = ax.plot([],[], lw=2, color='darkblue')

# Configuração dos limites do eixo Y para que a animação não mude de escala
# Máximo de |Psi|^2 ocorre quando wave1 e wave2 estão em fase e se somam.
#max_amplitude_square = (np.sqrt(2/L) * (1/np.sqrt(2) + 1/np.sqrt(2)))**2 # Calculando (2/L)


def evoluc_temp_pç_finito(frame, L, n1, n2):
    max_amplitude_square = (np.sqrt(2/L) * (1/np.sqrt(2) + 1/np.sqrt(2)))**2
    ax.set_ylim(0, max_amplitude_square * 1.1) 
    ax.set_xlim(0, L)
    x = np.linspace(0,L,200)
    
    # CORREÇÃO 1: Usar n1 e n2 para ter superposição real
    wave1 = np.sqrt(2/L)*np.sin(n1*np.pi*x/L)
    wave2 = np.sqrt(2/L)*np.sin(n2*np.pi*x/L) 
    
    # Para clareza, usando a fórmula padrão (matematicamente igual à sua, mas mais legível)
    e1 = (np.pi*h_cortado/L)**2 * n1**2 / (2*massa_eletron)
    e2 = (np.pi*h_cortado/L)**2 * n2**2 / (2*massa_eletron)
    
    c = 1/(np.sqrt(2))
    c1 = 1/np.sqrt(100)
    c2 = np.sqrt(99/100)
    t = times[frame]
    t *= 300
    
    # Superposição complexa
    psi = (c *wave1* np.exp(-1j*e1*t/h_cortado) + 
           c *wave2* np.exp(-1j*e2*t/h_cortado))
    
    # Densidade de Probabilidade (módulo ao quadrado)
    prob_t = (np.abs(psi))**2 

    delta_x = x[1] - x[0]
    valor_esperado_x = np.sum(prob_t*x*delta_x)
    nome = f'frames_gif/frame{frame:03d}'
    
    #line.set_data(x, prob_t)
    ax.plot(x, prob_t, color='pink', linewidth=2, zorder=3)
    ax.plot(x, abs(wave1)**2, alpha=0.25, color='blue', linestyle='--', zorder=1)
    ax.plot(x, abs(wave2)**2, alpha=0.25, color='green', linestyle='--', zorder=2)
    ax.axvline(valor_esperado_x, color='purple', linestyle='--', linewidth=2, zorder=4)
    ax.set_xlabel('x', fontsize = 20, color = 'black')
    ax.set_title('$|\phi_x|^2$: densidade de probabilidade', fontsize = 24)
    ax.tick_params(direction='inout', length=15, width=2, labelsize=16)
    ax.grid(color='green', alpha=0.2)
    ax.set_title(f'Tempo: {t:.2f} s', fontsize=12) # Opcional: mostrar o tempo
    #fig.savefig('frames_gif/frame_{frame:05d}.png')
    fig.savefig(nome)
    #plt.pause(0.00001)
    ax.clear()

    # Deve retornar uma tupla de artistas (line,)

#ani = FuncAnimation(fig, evoluc_temp_pç_finito, frames=len(times), interval=50, blit=True)

# CORREÇÃO CRÍTICA: Salve antes de fechar a figura!
#ani.save("animac_teste.gif", writer='pillow', fps=20, dpi=100) # Mudei fps para 20
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
        'gif.gif',
        format='GIF',
        append_images=frames,
        save_all=True,
        duration=50,
        loop=0
    )