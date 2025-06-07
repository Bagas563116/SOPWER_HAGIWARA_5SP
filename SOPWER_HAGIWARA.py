import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# FORMAT FILE EXELNYA DIPERHATIKAN

def process_file(file_path):
    df = pd.read_excel(file_path)

    X = df["x"].values  
    SP1 = df["SP1"].values
    SP2 = df["SP2"].values
    SP3 = df["SP3"].values
    SP4 = df["SP4"].values
    SP5 = df["SP5"].values

    def nan(x_array, y_array):
        y_filled = y_array.copy()
        for i in range(1, len(y_array) - 1):
            if np.isnan(y_array[i]) and not np.isnan(y_array[i - 1]) and not np.isnan(y_array[i + 1]):
                x0, x1, x2 = x_array[i - 1], x_array[i], x_array[i + 1]
                y0, y2 = y_array[i - 1], y_array[i + 1]
                y_filled[i] = y0 + ((x1 - x0) / (x2 - x0)) * (y2 - y0)
        return y_filled

    SP1 = nan(X, SP1)
    SP2 = nan(X, SP2)
    SP3 = nan(X, SP3)
    SP4 = nan(X, SP4)
    SP5 = nan(X, SP5)

    return X, SP1, SP2, SP3, SP4, SP5

X, SP1, SP2, SP3, SP4, SP5 = [], [], [], [], [], []

def browse_file():
    global X, SP1, SP2, SP3, SP4, SP5
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            X, SP1, SP2, SP3, SP4, SP5 = process_file(file_path)
            show_plot(X, SP1, SP2, SP3, SP4, SP5)
            label_file.config(text=f"File diproses: {file_path}")

        except Exception as e:
            label_file.config(text=f"Error: {e}")

def show_plot(X, SP1, SP2, SP3, SP4, SP5):

    plot_window = tk.Toplevel(root)
    plot_window.title("Scatter Plot")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X, SP1, label="SP1", color="r", s=10)
    ax.scatter(X, SP2, label="SP2", color="g", s=10)
    ax.scatter(X, SP3, label="SP3", color="b", s=10)
    ax.scatter(X, SP4, label="SP4", color="m", s=10)
    ax.scatter(X, SP5, label="SP5", color="c", s=10)
    ax.set_xlabel("X")
    ax.set_ylabel("SP Values")
    ax.legend()
    ax.set_title("Scatter Plot of SP Values vs X")

    canvas = FigureCanvasTkAgg(fig, master=plot_window)  # menyematkan plot ke jendela baru
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def collect_inputs():
    inputs = []
    for entry in entry_widgets:
        try:
            value = float(entry.get())  
            inputs.append(value)
        except ValueError:
            inputs.append(None) 
    print("Collected Inputs:", inputs) 

"""------------------------------------------------------------------------------------------------------------------------"""

root = tk.Tk()
root.title("HAGIWARA SOPWER")
root.geometry("400x600")
root.resizable(False, False)
frame = ttk.Frame(root, padding=(50, 50))
frame.grid(row=0, column=0, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

""""-----------------------------------------------------------------------------------------------------------------------"""

button_browse = tk.Button(frame, text="Browse Excel File", command=browse_file)
button_browse.grid(row=0, columnspan=2, pady=10)

label_file = tk.Label(frame, text="Pilih file Excel untuk mengakses data.")
label_file.grid(row=1, columnspan=2, pady=10)

""""-----------------------------------------------------------------------------------------------------------------------"""

entry_widgets = [] 

label_input1 = tk.Label(frame, text="Posisi SP2:")
label_input1.grid(row=2, column=0, pady=5, sticky="w")
entry_input1 = tk.Entry(frame)
entry_input1.grid(row=2, column=1, pady=5)
entry_input1.insert(tk.END, "0")  
entry_widgets.append(entry_input1)

label_input2 = tk.Label(frame, text="Posisi SP3:")
label_input2.grid(row=3, column=0, pady=5, sticky="w")
entry_input2 = tk.Entry(frame)
entry_input2.grid(row=3, column=1, pady=5)
entry_input2.insert(tk.END, "23")
entry_widgets.append(entry_input2)

label_input3 = tk.Label(frame, text="Posisi SP4:")
label_input3.grid(row=4, column=0, pady=5, sticky="w")
entry_input3 = tk.Entry(frame)
entry_input3.grid(row=4, column=1, pady=5)
entry_input3.insert(tk.END, "46")
entry_widgets.append(entry_input3)

label_input4 = tk.Label(frame, text="Total kedalaman:")
label_input4.grid(row=5, column=0, pady=5, sticky="w")
entry_input4 = tk.Entry(frame)
entry_input4.grid(row=5, column=1, pady=5)
entry_input4.insert(tk.END, "-40")
entry_widgets.append(entry_input4)

label_input5 = tk.Label(frame, text="Total Kedalaman pada grafik:")
label_input5.grid(row=6, column=0, pady=5, sticky="w")
entry_input5 = tk.Entry(frame)
entry_input5.grid(row=6, column=1, pady=5)
entry_input5.insert(tk.END, "-20")
entry_widgets.append(entry_input5)

label_input6 = tk.Label(frame, text="Index Akhir Direct Forward SP2:")
label_input6.grid(row=7, column=0, pady=5, sticky="w")
entry_input6 = tk.Entry(frame)
entry_input6.grid(row=7, column=1, pady=5)
entry_input6.insert(tk.END, "11")
entry_widgets.append(entry_input6) 

label_input7 = tk.Label(frame, text="Index Akhir Refracted Reverse SP3:")
label_input7.grid(row=8, column=0, pady=5, sticky="w")
entry_input7 = tk.Entry(frame)
entry_input7.grid(row=8, column=1, pady=5)
entry_input7.insert(tk.END, "10")
entry_widgets.append(entry_input7)

label_input8 = tk.Label(frame, text="Index Akhir Direct Reverse SP3:")
label_input8.grid(row=9, column=0, pady=5, sticky="w")
entry_input8 = tk.Entry(frame)
entry_input8.grid(row=9, column=1, pady=5)
entry_input8.insert(tk.END, "13")
entry_widgets.append(entry_input8)

label_input9 = tk.Label(frame, text="Index Akhir Direct Forward SP3:")
label_input9.grid(row=10, column=0, pady=5, sticky="w")
entry_input9 = tk.Entry(frame)
entry_input9.grid(row=10, column=1, pady=5)
entry_input9.insert(tk.END, "19")
entry_widgets.append(entry_input9)

label_input10 = tk.Label(frame, text="Index Akhir Refracted Reverse SP4:")
label_input10.grid(row=11, column=0, pady=5, sticky="w")
entry_input10 = tk.Entry(frame)
entry_input10.grid(row=11, column=1, pady=5)
entry_input10.insert(tk.END, "16")
entry_widgets.append(entry_input10)

"""------------------------------------------------------------------------------------------------------------------------"""

button_collect = tk.Button(frame, text="Plot Hasil", command=lambda: collect_inputs(X, SP1, SP2, SP3, SP4, SP5))
button_collect.grid(row=12, columnspan=2, pady=10)

def collect_inputs(X, SP1, SP2, SP3, SP4, SP5):
    inputs = []
    for entry in entry_widgets:
        try:
            value = int(entry.get()) 
            inputs.append(value)
        except ValueError:
            inputs.append(None)  
    print("Collected Inputs:", inputs)  
    
    # Ambil input
    posisi_SP2 = inputs[0]

    posisi_SP2 = inputs[0]
    posisi_SP3 = inputs[1]
    posisi_SP4 = inputs[2]
    Y = inputs[3]
    Y_lim = inputs[4]

    i_awal_DF_SP2 = 0
    i_akhir_DF_SP2 = inputs[5]
    i_awal_RF_SP2 = inputs[5]
    i_akhir_RF_SP2 = len(X)

    i_awal_RR_SP3 = 0
    i_akhir_RR_SP3 = inputs[6]
    i_awal_DR_SP3 = inputs[6]
    i_akhir_DR_SP3 = inputs[7]

    i_awal_RR_SP4 = 0
    i_akhir_RR_SP4 = inputs[9]
    i_awal_DR_SP4 = inputs[9]
    i_akhir_DR_SP4 = len(X)

    i_awal_DF_SP3 = inputs[7] - 1
    i_akhir_DF_SP3 = inputs[8]
    i_awal_RF_SP3 = inputs[8]
    i_akhir_RF_SP3 = len(X)

    # MENCARI PERSAMAAN GARIS DIRECT DAN FORWARD MASING MASING SP

    DF_SP2 = SP2[i_awal_DF_SP2 : i_akhir_DF_SP2]
    RF_SP2 = SP2[i_awal_RF_SP2 : i_akhir_RF_SP2]

    DR_SP3 = SP3[i_awal_DR_SP3 : i_akhir_DR_SP3]
    RR_SP3 = SP3[i_awal_RR_SP3 : i_akhir_RR_SP3]

    DR_SP4 = SP4[i_awal_DR_SP4 : i_akhir_DR_SP4]
    RR_SP4 = SP4[i_awal_RR_SP4 : i_akhir_RR_SP4]

    DF_SP3 = SP3[i_awal_DF_SP3 : i_akhir_DF_SP3]
    RF_SP3 = SP3[i_awal_RF_SP3 : i_akhir_RF_SP3]

    m_DF_SP2, c_DF_SP2 = np.polyfit(X[i_awal_DF_SP2 : i_akhir_DF_SP2], DF_SP2, 1)
    m_RF_SP2, c_RF_SP2 = np.polyfit(X[i_awal_RF_SP2 : i_akhir_RF_SP2], RF_SP2, 1)

    m_DR_SP3, c_DR_SP3 = np.polyfit(X[i_awal_DR_SP3 : i_akhir_DR_SP3], DR_SP3, 1)
    m_RR_SP3, c_RR_SP3 = np.polyfit(X[i_awal_RR_SP3 : i_akhir_RR_SP3], RR_SP3, 1)

    m_DR_SP4, c_DR_SP4 = np.polyfit(X[i_awal_DR_SP4 : i_akhir_DR_SP4], DR_SP4, 1)
    m_RR_SP4, c_RR_SP4 = np.polyfit(X[i_awal_RR_SP4 : i_akhir_RR_SP4], RR_SP4, 1)

    m_DF_SP3, c_DF_SP3 = np.polyfit(X[i_awal_DF_SP3 : i_akhir_DF_SP3], DF_SP3, 1)
    m_RF_SP3, c_RF_SP3 = np.polyfit(X[i_awal_RF_SP3 : i_akhir_RF_SP3], RF_SP3, 1)



    # MENCARI PHANTOIM ARRIVAL

    def phantom_near(awal, akhir, SP, near):
        new_SP = SP[awal : akhir]
        Y = near[awal : akhir] 
        DT = Y[-1] - new_SP[-1]
        phantom_arrival = Y[1:] - DT
        return phantom_arrival

    def phantom_far(awal, akhir, SP, far):
        new_SP = SP[awal : akhir]
        Y = far[awal : akhir] 
        DT = Y[0] - new_SP[0]
        phantom_arrival = Y[:len(Y)-1] - DT
        return phantom_arrival

    forward23 = np.append(phantom_near(i_awal_DF_SP2, i_akhir_DF_SP2, SP2, SP1), SP2[i_awal_RF_SP2 : i_akhir_DR_SP3 - 1])
    reverse23 = np.append(SP3[i_awal_DF_SP2 + 1 : i_akhir_RR_SP3], phantom_far(i_awal_DR_SP3, i_akhir_DR_SP3, SP3, SP4))

    forward24 = np.append(phantom_near(i_awal_DF_SP2, i_akhir_DF_SP2, SP2, SP1), SP2[i_awal_RF_SP2 : i_akhir_DR_SP4 - 1])
    reverse24 = np.append(SP4[i_awal_DF_SP2 + 1 : i_akhir_RR_SP4], phantom_far(i_awal_DR_SP4, i_akhir_DR_SP4, SP4, SP5))

    forward34 = np.append(phantom_near(i_awal_DF_SP3, i_akhir_DF_SP3, SP3, SP2), SP3[i_awal_RF_SP3 : i_akhir_DR_SP4 - 1])
    reverse34 = np.append(SP4[i_awal_DF_SP3 + 1 : i_akhir_RR_SP4], phantom_far(i_awal_DR_SP4, i_akhir_DR_SP4, SP4, SP5))



    # MENCARI TAB & TP

    def tab(m_forward, c_forward, m_reverse, c_reverse, x_forward, x_reverse):
        STS_forward = np.round(m_forward, 4) * x_reverse + np.round(c_forward, 4)
        STS_reverse = np.round((m_reverse), 4) * x_forward + np.round(c_reverse, 4)
        tab = (STS_forward + STS_reverse)/2
        return np.round(tab, 4)

    def tp(m_forward, c_forward, m_reverse, c_reverse, x_forward, x_reverse, tap, tpb):
        STS_forward = np.round(m_forward, 4) * x_reverse + np.round(c_forward, 4)
        STS_reverse = np.round((m_reverse), 4) * x_forward + np.round(c_reverse, 4)
        tab = (STS_forward + STS_reverse)/2
        tp = (tap + tpb) - tab
        return tp

    tab_SP23 = tab(m_RF_SP2, c_RF_SP2, m_RR_SP3, c_RR_SP3, posisi_SP2, posisi_SP3)
    tab_SP24 = tab(m_RF_SP2, c_RF_SP2, m_RR_SP4, c_RR_SP4, posisi_SP2, posisi_SP4)
    tab_SP34 = tab(m_RF_SP3, c_RF_SP3, m_RR_SP4, c_RR_SP4, posisi_SP3, posisi_SP4)


    tp_SP23 = tp(m_RF_SP2, c_RF_SP2, m_RR_SP3, c_RR_SP3, posisi_SP2, posisi_SP3, forward23, reverse23)
    tp_SP24 = tp(m_RF_SP2, c_RF_SP2, m_RR_SP4, c_RR_SP4, posisi_SP2, posisi_SP4, forward24, reverse24)
    tp_SP34 = tp(m_RF_SP3, c_RF_SP3, m_RR_SP4, c_RR_SP4, posisi_SP3, posisi_SP4, forward34, reverse34)



    # MENCARI T'AP

    def t_ap(m_forward, c_forward, m_reverse, c_reverse, x_forward, x_reverse, tap, tpb):
        STS_forward = np.round(m_forward, 4) * x_reverse + np.round(c_forward, 4)
        STS_reverse = np.round((-m_reverse), 4) * x_forward + np.round(c_reverse, 4)
        tab = (STS_forward + STS_reverse)/2
        tp = (tap + tpb) - tab
        t_ap = tap - tp/2
        return t_ap

    t_ap_SP23 = t_ap(m_RF_SP2, c_RF_SP2, m_RR_SP3, c_RR_SP3, posisi_SP2, posisi_SP3, forward23, reverse23)
    t_ap_SP24 = t_ap(m_RF_SP2, c_RF_SP2, m_RR_SP4, c_RR_SP4, posisi_SP2, posisi_SP4, forward24, reverse24)
    t_ap_SP34 = t_ap(m_RF_SP3, c_RF_SP3, m_RR_SP4, c_RR_SP4, posisi_SP3, posisi_SP4, forward34, reverse34)



    # MENCARI PERSAMAAN GARIS T'AP

    m_t_ap_SP23, c_t_ap_SP23 = np.polyfit(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP3 - 1], t_ap_SP23, 1)
    m_t_ap_SP24, c_t_ap_SP24 = np.polyfit(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP4 - 1], t_ap_SP24, 1)
    m_t_ap_SP34, c_t_ap_SP34 = np.polyfit(X[i_awal_DF_SP3 + 1 : i_akhir_DR_SP4 - 1], t_ap_SP34, 1)

    y_t_ap_SP23 = m_t_ap_SP23 * X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP3 - 1] + c_t_ap_SP23
    y_t_ap_SP24 = m_t_ap_SP24 * X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP4 - 1] + c_t_ap_SP24
    y_t_ap_SP34 = m_t_ap_SP34 * X[i_awal_DF_SP3 + 1 : i_akhir_DR_SP4 - 1] + c_t_ap_SP34



    # MENCARI V1 V2 & TETA

    V1_SP23 = (1/np.round(m_DF_SP2,4) - 1/np.round(m_DR_SP3,4))/2
    V1_SP24 = (1/np.round(m_DF_SP2,4) - 1/np.round(m_DR_SP4,4))/2
    V1_SP34 = (1/np.round(m_DF_SP3,4) - 1/np.round(m_DR_SP4,4))/2

    V2_SP23 = 1/np.round(m_t_ap_SP23,4)
    V2_SP24 = 1/np.round(m_t_ap_SP24,4)
    V2_SP34 = 1/np.round(m_t_ap_SP34,4)

    teta_SP23 = (1 - (V1_SP23/V2_SP23)**2)**0.5
    teta_SP24 = (1 - (V1_SP24/V2_SP24)**2)**0.5
    teta_SP34 = (1 - (V1_SP34/V2_SP34)**2)**0.5



    # MENCARI HP DAN H2

    hp_SP23 = -(V1_SP23/(2*teta_SP23))*tp_SP23
    hp_SP24 = -(V1_SP24/(2*teta_SP24))*tp_SP24
    hp_SP34 = -(V1_SP34/(2*teta_SP34))*tp_SP34

    h2_SP23 = Y - hp_SP23
    h2_SP24 = Y - hp_SP24
    h2_SP34 = Y - hp_SP34
    
    fig3, axs3 = plt.subplots(nrows=3, ncols=1, figsize=(10, 9))
    axs3[0].fill_between(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP3 - 1], hp_SP23, color='steelblue')
    axs3[0].fill_between(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP3 - 1], hp_SP23, h2_SP23, color='darkorange')
    axs3[0].set_title("Model Lapisan Kecepatan SP2 SP3", fontsize=14, weight='bold')
    axs3[0].set_xlabel("Jarak (m)", fontsize=11, weight='bold')
    axs3[0].set_ylabel("Kedalaman (m)", fontsize=11)
    axs3[0].set_ylim(Y_lim, 0)
    axs3[0].set_xticks(X[1:len(X)])
    axs3[1].fill_between(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP4 - 1], hp_SP24, color='steelblue')
    axs3[1].fill_between(X[i_awal_DF_SP2 + 1 : i_akhir_DR_SP4 - 1], hp_SP24, h2_SP24, color='darkorange')
    axs3[1].set_title("Model Lapisan Kecepatan SP2 SP4", fontsize=14, weight='bold')
    axs3[1].set_xlabel("Jarak (m)", fontsize=11, weight='bold')
    axs3[1].set_ylabel("Kedalaman (m)", fontsize=11)
    axs3[1].set_ylim(Y_lim, 0)
    axs3[1].set_xticks(X[1:len(X)])
    axs3[2].fill_between(X[i_awal_DF_SP3 + 1 : i_akhir_DR_SP4 - 1], hp_SP34, color='steelblue')
    axs3[2].fill_between(X[i_awal_DF_SP3 + 1 : i_akhir_DR_SP4 - 1], hp_SP34, h2_SP34, color='darkorange')
    axs3[2].set_title("Model Lapisan Kecepatan SP3 SP4", fontsize=14, weight='bold')
    axs3[2].set_xlabel("Jarak (m)", fontsize=11, weight='bold')
    axs3[2].set_ylabel("Kedalaman (m)", fontsize=11)
    axs3[2].set_ylim(Y_lim, 0)
    axs3[2].set_xticks(X[1:len(X)])

    plt.tight_layout()
    plt.show()  


root.mainloop()
