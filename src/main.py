import pandas as pd
from preprocess import clean_text, extract_syllable_count
from features import word_overlap, missing_words, length_ratio, sequence_similarity
from scoring import compute_score, generate_explanation
from semantic import semantic_similarity

file_path = "data/AutoEIT Sample Transcriptions for Scoring.xlsx"

# Load all sheets
all_sheets = pd.read_excel(file_path, sheet_name=None)

print("Sheets found:", all_sheets.keys())

# Remove 'Info' sheet
sheets = {k: v for k, v in all_sheets.items() if k != "Info"}

print("\nSheets used:", sheets.keys())

# Inspect one sheet
updated_sheets = {}

for name, df in sheets.items():
    print(f"\n--- Sheet: {name} ---")
    
    df['syllable_count'] = df['Stimulus'].apply(extract_syllable_count)
    df['clean_stimulus'] = df['Stimulus'].apply(clean_text)
    df['clean_response'] = df['Transcription Rater 1'].apply(clean_text)
    
    # Feature calculations
    df['word_overlap'] = df.apply(lambda x: word_overlap(x['clean_stimulus'], x['clean_response']), axis=1)
    df['missing_words'] = df.apply(lambda x: missing_words(x['clean_stimulus'], x['clean_response']), axis=1)
    df['length_ratio'] = df.apply(lambda x: length_ratio(x['clean_stimulus'], x['clean_response']), axis=1)
    df['sequence_similarity'] = df.apply(lambda x: sequence_similarity(x['clean_stimulus'], x['clean_response']), axis=1)

    df['semantic_similarity'] = df.apply(lambda x: semantic_similarity(x['clean_stimulus'], x['clean_response']), axis=1)

    df['predicted_score'] = df.apply(compute_score, axis=1)

    df['Explanation'] = df.apply(generate_explanation, axis=1)
    
    print(df[
    [
        'clean_stimulus',
        'clean_response',
        'word_overlap',
        'missing_words',
        'length_ratio',
        'sequence_similarity',
        'semantic_similarity',
        'predicted_score'
    ]].head())
    
    updated_sheets[name] = df

output_path = "outputs/scored_output.xlsx"

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    for name, df in updated_sheets.items():
        df.to_excel(writer, sheet_name=name, index=False)

print(f"\n✅ Scored file saved at: {output_path}")