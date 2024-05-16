# exemple-chatbot-rag
Un tutoriel pour créer un chatbot "philosophe" en Python en utilisant la méthode RAG


## 1) Récupérer les oeuvres
Pour que votre chatbot soit le plus précis possible il va falloir en premier lieu récupérer les oeuvres (complètes, si possible) au format texte numérique.

Vous pouvez [cliquez ici](https://github.com/La-caverne-de-Platon/auteurs_platon/fork) pour créer automatiquement une copie du repo exemple qui contient certaines oeuvres de Platon

## 2) Utiliser un service de RAG
Soit vous utilisez une solution "maison" mais vous devez être propriétaire d'un serveur disposant d'une très bonne carte graphique, soit vous utilisez des services en ligne.
J'utilise Phorm, qui sert à la base à discuter avec les projets sur Github, mais le procédé derrière est le même : discuter avec du contenu textuel.

### a) Créer le WorkSpace sur Phorm
1. Allez sur [le site de Phorm](https://www.phorm.ai/).
2. Renseignez dans le champ l'url du repo, soit ma copie soit un repo bien à vous avec les documents sous forme de **texte brut** (pas de PDF, mais Markdown ça fonctionne)
3. Cliquez sur le bouton pour créer le "Workspace"

### b) Récupérer les informations nécessaires
1. Cliquez sur votre nouveau WorkSpace, l'url devrait ressembler à ceci : 
```
https://www.phorm.ai/query?projectId=3ae8fecb-7961-4938-ad55-22beb3217a8a
```
2. Gardez la valeur de "projectId" ainsi que l'url qui pointe vers le repo Github, soit le votre soit ma copie. Pour l'exemple, cela fait donc : 

```
3ae8fecb-7961-4938-ad55-22beb3217a8a
https://github.com/La-caverne-de-Platon/auteurs_platon/tree/main
```

## 3) Modifier le contenu des scripts

Vous trouverez [les informations à changer ici dans le script Python](https://github.com/La-caverne-de-Platon/exemple-chatbot-rag/blob/fc33d693085a18cfea134692451a04afc5bb1a24/exemple_platon.py#L31):

```python
# Ici les informations vis à vis du philosophe, il faut toujours relier le projet Phorm à un repo Github
payload = {
    "query": query,
    "project": "8f603354-e047-48cc-ad66-717a8ecdb598",
    "repos": ["https://github.com/la-caverne-de-platon/auteurs_platon/tree/main"]
}
```

Ou encore [ici pour le script JavaScript](https://github.com/La-caverne-de-Platon/exemple-chatbot-rag/blob/bad873ccb2b65c0d57d57db560f47769d16d7b12/index.html#L118) :

```js
body: JSON.stringify({
    query: message + ' Explique comme à un enfant de 16 ans; ne donne pas d extrait de code. ' + ' Tu dois répondre en utilisant uniquement le point de vue de ' + author,
    project: '3ae8fecb-7961-4938-ad55-22beb3217a8a',
    repos: ['https://github.com/la-caverne-de-platon/auteurs_platon/tree/main']
})
```
