def compute_score(row):
    overlap = row['word_overlap']
    missing = row['missing_words']
    seq_sim = row['sequence_similarity']
    sem_sim = row['semantic_similarity']
    length_ratio = row['length_ratio']
    
    # ===== SCORE 4 (Exact / near exact) =====
    if sem_sim > 0.95 and overlap > 0.9 and missing == 0:
        return 4
    
    # ===== SCORE 3 (Meaning preserved) =====
    if sem_sim > 0.80:
        return 3
    
    # ===== SCORE 2 (Partial meaning) =====
    if sem_sim > 0.60:
        return 2
    
    # ===== SCORE 1 (Weak meaning) =====
    if sem_sim > 0.40:
        return 1
    
    # ===== SCORE 0 (No meaning) =====
    return 0

def generate_explanation(row):
    sem = row['semantic_similarity']
    overlap = row['word_overlap']
    missing = row['missing_words']
    
    if sem > 0.95:
        return "Perfect or near-perfect repetition"
    
    if sem > 0.80:
        return "Meaning preserved with minor differences"
    
    if sem > 0.60:
        return "Partial meaning captured, some missing content"
    
    if sem > 0.40:
        return "Limited meaning retained"
    
    return "Response unrelated or incorrect"