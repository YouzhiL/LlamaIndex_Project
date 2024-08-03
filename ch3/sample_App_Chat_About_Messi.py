from llama_index.core import Document, SummaryIndex
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.readers.wikipedia import WikipediaReader
# simple Q & A system, not a genuine chat system because it does not retain the context 
# of the conversation.
loader = WikipediaReader()
documents = loader.load_data(pages=["Messi Lionel"]) # load a Wiki page on Lionel Messi as a Document using the Wiki data loader
parser = SimpleNodeParser.from_defaults() # parse the document into smaller Node chunks. This splits the text into logical segments
nodes = parser.get_nodes_from_documents(documents) # build SummaryIndex from the nodes
index = SummaryIndex(nodes) # define QueryEngine, forming a complete query pipeline
query_engine = index.as_query_engine()
print("Ask me anything about Lionel Messi!")

while True:
    question = input("Your question: ")
    if question.lower() == "exit":
        break
    response = query_engine.query(question)
    print(response)
