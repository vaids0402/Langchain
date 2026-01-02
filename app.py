# from src.data_loader import load_all_documents
# from src.vectorstore import FaissVectorStore
# from src.search import RAGSearch

# # Example usage
# if __name__ == "__main__":
    
#     docs = load_all_documents("data")
#     store = FaissVectorStore("faiss_store")
#     #store.build_from_documents(docs)
#     store.load()
#     #print(store.query("What is attention mechanism?", top_k=3))
#     rag_search = RAGSearch()
#     query = "What is attention mechanism?"
#     summary = rag_search.search_and_summarize(query, top_k=3)
#     print("Summary:", summary)

from src.search import RAGSearch


def main():
    """
    Entry point for running the RAG system manually.
    This is intended for demo / interactive usage.
    Evaluation logic lives separately in evals/.
    """
    rag_search = RAGSearch()

    query = "What is attention mechanism?"
    answer = rag_search.search_and_summarize(
        query=query,
        top_k=3
    )

    print("\n==============================")
    print("Query:")
    print(query)
    print("\nAnswer:")
    print(answer)
    print("==============================\n")


if __name__ == "__main__":
    main()
