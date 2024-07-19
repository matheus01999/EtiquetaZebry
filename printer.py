from xml.dom import minidom

#cria documento
doc = minidom.Document()

#cria raiz e adicionar no documento
raiz = doc.createElement('raiz')
doc.appendChild(doc.createElement('raiz'))

#cria itens e adiciona na raiz
itens = doc.createElement('itens')
raiz.appendChild(itens)

#cria itens e textos
for i in range(3):
    item = doc.createElement('item')
    item.setAttribute('name', 'item' + str(i+1))
    itens.appendChild(item)
    item.appendChild( doc.createTextNode('Item ' + str(i + 1)))

#xmldoc = minidom.Document()
print(raiz.toprettyxml())