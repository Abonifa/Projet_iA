import tkinter as tk
from chat_script import ask_question

def envoi_question():
    question = entry.get()  # Récupérer la question saisie par l'utilisateur depuis la zone de texte
    response = ask_question(question)  # Poser la question au chatbot et récupérer la réponse
    output.insert(tk.END, response + "\n \n \n")  # Afficher la réponse dans la zone de texte

def quit_program():
    """
    Fonction pour quitter le programme.
    """
    root.quit()
 
root = tk.Tk()
root.title("Chatbot pour le football ou les sports en général ")
 
label = tk.Label(root, text="Posez une question sur les sports ou le football en général:")
label.pack()
 
entry = tk.Entry(root)
entry.pack()
 
button = tk.Button(root, text="Envoyer", command=envoi_question)
button.pack()
 
quit_button = tk.Button(root, text="Quitter", command=quit_program)
quit_button.pack()
 
output = tk.Text(root, height=10, width=50)
output.pack()
 
root.mainloop()