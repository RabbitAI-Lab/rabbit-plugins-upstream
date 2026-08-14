# CEFR Levels and Media Recommendations

## The CEFR Framework

The Common European Framework of Reference for Languages (CEFR) is the international standard for describing language proficiency. Six levels from A1 (beginner) to C2 (mastery).

## Level Descriptions and Media Guidance

### A1 — Beginner

- **Can**: Understand basic phrases, introduce yourself, ask simple questions
- **Vocabulary**: ~500 words
- **Media recommendation**: None yet. Focus on structured courses.
- **TV**: Peppa Pig, extr@ (language learning series), dubbed children's shows

### A2 — Elementary

- **Can**: Handle routine tasks, describe background, read simple text
- **Vocabulary**: ~1,000 words
- **Media recommendation**: Children's content, language learning channels
- **TV**: Disney movies (dubbed), simplified news (News in Slow Spanish/French)
- **Study approach**: Pre-study 80%+ of vocabulary before watching

### B1 — Intermediate

- **Can**: Follow main points of clear standard speech, deal with most travel situations
- **Vocabulary**: ~2,000 words
- **Media recommendation**: Sitcoms, reality TV, simple dramas
- **TV**: Friends (dubbed or in target language), Modern Family, reality shows
- **Study approach**: Pre-study 50% of vocabulary; watch with target-language subtitles

### B2 — Upper Intermediate

- **Can**: Understand main ideas of complex text, interact with native speakers fluently
- **Vocabulary**: ~4,000 words
- **Media recommendation**: Most TV dramas, films, documentaries
- **TV**: Breaking Bad, The Crown, most Netflix originals in target language
- **Study approach**: Pre-study only high-frequency unknowns; try without subtitles

### C1 — Advanced

- **Can**: Express ideas fluently, understand implicit meaning, use language flexibly
- **Vocabulary**: ~8,000 words
- **Media recommendation**: All content including news, comedy, literature adaptations
- **TV**: Everything accessible, including humor and wordplay-heavy content
- **Study approach**: Focus on idioms, register, cultural references

### C2 — Mastery

- **Can**: Understand virtually everything, distinguish subtle shades of meaning
- **Vocabulary**: 16,000+ words
- **Media**: Unrestricted — same as a native speaker

## How Language Immersion TV Estimates CEFR

The tool uses **frequency percentile** within the analyzed content to estimate difficulty:

```python
def estimate_cefr(frequency_rank, total_unique_words):
    percentile = frequency_rank / total_unique_words
    if frequency_rank <= 100:
        return "A1"
    elif frequency_rank <= 500:
        return "A2"
    elif frequency_rank <= 1500:
        return "B1"
    elif frequency_rank <= 4000:
        return "B2"
    elif frequency_rank <= 10000:
        return "C1"
    else:
        return "C2"
```

### Important Caveats

- Frequency in **one show** ≠ frequency in the **language overall**. A medical drama will over-represent medical terms.
- For accurate CEFR estimation, the tool works best with larger corpora (full seasons, not single episodes).
- CEFR levels are approximate. Use them as a guide, not a definitive label.

## Media Type by Level — Quick Reference

| Level | Best Media | Avoid |
|-------|-----------|-------|
| A1-A2 | Children's animation, learning series | Everything else |
| B1 | Sitcoms, reality TV, soap operas | Complex dramas, comedies with wordplay |
| B2 | Most dramas, action films, documentaries | Dense dialogue, heavy accents/slang |
| C1 | News, comedy, period dramas | Obscure dialects, avant-garde cinema |
| C2 | Everything | Nothing |

## Choosing Your First Show

1. **Pick something you've already seen** in your native language — you know the plot, which aids comprehension
2. **Choose a sitcom** over a drama — everyday vocabulary, shorter sentences, clearer pronunciation
3. **Avoid**: medical/legal procedurals (jargon), period pieces (archaic language), stand-up comedy (wordplay)
4. **Prefer**: 20–25 min episodes (sitcoms) over 50 min dramas — easier to study in chunks
