from markitdown import MarkItDown

files = []

md = MarkItDown(enable_plugins=True)

for filepath in files:
    result = md.convert(source= filepath).markdown
    with open("/backend/knowledgebase/knowledge.txt", 'a') as file:
        file.write(result)
        file.close()
       

print('done writing')
