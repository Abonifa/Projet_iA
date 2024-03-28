import os

from openai import OpenAI

def ask_question(question):

    # Récupérer la clé API à partir de la variable d'environnement
    my_key = os.getenv("OPENAI_API_KEY")

    # Initialisation du client OpenAI avec votre clé API
    client = OpenAI(api_key=my_key)

    # Variable pour stocker le contexte des questions précédentes
    contexte = ""

    # Message de bienvenue
    print("Bienvenue dans votre chatbot qui répond à toutes vos questions sur les sports ou le football")

    # Boucle principale pour interagir avec l'utilisateur
    while True:

        # Vérifier si l'utilisateur souhaite quitter
        if question.lower() == "exit":
            print("Merci d'avoir utilisé notre service. Au revoir !")
            break

        # Créer une requête vers l'API de ChatGPT avec le contexte des questions précédentes
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": contexte},
                {"role": "user", "content": question}
            ]
        )

        # Récupérer et afficher la réponse du chatbot
        response = completion.choices[0].message.content
        print("Réponse du chatbot :")
        print(response) # return response 

        # Demander à l'utilisateur de saisir une nouvelle question        
        question = input("Posez une question sur les sports ou le football (ou 'exit' pour quitter) : ")

        # Mettre à jour le contexte avec la nouvelle question et la réponse
        contexte += f" {question} {response}"

if __name__ == "__main__":
    # Demander à l'utilisateur de saisir une question
    question = input("Posez-moi une question sur  les sports ou le football : ")
    # Poser la question à l'API et afficher la réponse obtenue
    print(ask_question(question))