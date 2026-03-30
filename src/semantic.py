from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')


def semantic_similarity(stimulus, response):
    embeddings = model.encode([stimulus, response])
    
    score = util.cos_sim(embeddings[0], embeddings[1])
    
    return float(score)