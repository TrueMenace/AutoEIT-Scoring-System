from collections import Counter
from difflib import SequenceMatcher


def word_overlap(stimulus, response):
    stim_words = stimulus.split()
    resp_words = response.split()
    
    common = set(stim_words) & set(resp_words)
    return len(common) / max(len(stim_words), 1)


def missing_words(stimulus, response):
    stim_words = set(stimulus.split())
    resp_words = set(response.split())
    
    missing = stim_words - resp_words
    return len(missing)


def length_ratio(stimulus, response):
    stim_len = len(stimulus.split())
    resp_len = len(response.split())
    
    if stim_len == 0:
        return 0
    return resp_len / stim_len


def sequence_similarity(stimulus, response):
    return SequenceMatcher(None, stimulus, response).ratio()