"""Templates related to query generation."""

QUERY_REWRITING_TEMPLATE = """
You are an AI assistant specialized in information retrieval.

Your task is to generate {num_questions} diverse rephrasings of the user's question to improve document retrieval from a vector database.
These rewrites should vary in phrasing and perspective to increase the chances of finding relevant matches during similarity search.
Each rephrased question should be listed on a separate line.

Original question: {question}
"""
