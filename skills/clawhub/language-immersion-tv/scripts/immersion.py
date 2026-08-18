#!/usr/bin/env python3
"""
Language Immersion TV — extract vocabulary from subtitle files.

Subcommands:
  analyze       — analyze a single subtitle file, show frequency stats
  build-season  — build a combined frequency list from multiple subtitle files
  export        — export flashcard deck (Anki TSV, CSV, or JSON)
  compare       — find words common across multiple subtitle files

Usage:
  python immersion.py analyze movie.srt --language en
  python immersion.py build-season subs/ --language es --output deck.json
  python immersion.py export movie.srt --language fr --format anki --output cards.tsv
  python immersion.py compare subs/ --language en --top 100
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Stop words for supported languages
# ---------------------------------------------------------------------------

STOP_WORDS = {
    "en": {
        "the","a","an","and","or","but","if","then","of","to","in","on","at","by","for","with",
        "from","as","is","are","was","were","be","been","being","have","has","had","do","does",
        "did","will","would","could","should","may","might","can","shall","i","you","he","she",
        "it","we","they","me","him","her","us","them","my","your","his","its","our","their",
        "this","that","these","those","what","which","who","whom","whose","where","when","why",
        "how","all","any","some","no","not","nor","so","too","very","just","only","also","here",
        "there","now","than","then","once","out","up","down","off","over","under","again","more",
        "most","other","such","own","same","about","into","through","during","before","after",
        "above","below","between","because","while","any","both","each","few","further","ll","ve",
        "re","s","t","d","m","don","won","ain","isn","aren","wasn","weren","doesn","didn","hasn",
        "haven","shouldn","couldn","wouldn","mustn","needn","mightn","let","get","got","getting",
        "going","go","goes","went","gone","like","want","wanted","know","knew","known","think",
        "thought","said","say","says","make","made","making","see","saw","seen","look","looked",
        "come","came","coming","take","took","taken","come","came","one","two","three","yeah",
        "yes","ok","okay","oh","ah","uh","um","hey","hi","hello","well","right","back","still",
        "got","really","lot","much","many","every","ever","never","always","let","going","gonna",
        "wanna","gotta","kind","sort","tell","told","telling","thing","things","stuff","man",
        "woman","guy","guys","mr","mrs","ms","sir","ma'am","hmm","huh","ooh","wow","whoa","yep",
        "nope","nah","bye","goodbye","please","thank","thanks","welcome","sorry","excuse","whoa",
    },
    "es": {
        "el","la","los","las","un","una","unos","unas","y","o","pero","si","de","del","al","en",
        "con","por","para","sin","sobre","entre","hasta","desde","como","más","menos","muy","ya",
        "que","qué","quien","quiénes","cuyo","donde","dónde","cuando","cuándo","como","cómo",
        "cual","cuál","porque","pues","aunque","mientras","tan","tanto","poco","mucho","nada",
        "todo","todos","toda","todas","algo","alguien","nadie","también","tampoco","sí","no",
        "yo","tú","él","ella","ello","nosotros","vosotros","ellos","ellas","usted","ustedes",
        "me","te","se","nos","os","les","le","lo","mi","mis","tu","tus","su","sus","nuestro",
        "vuestra","suyo","aquel","aquella","eso","esa","este","esta","estos","estas","eso","esa",
        "esos","esas","ser","es","son","fue","fueron","era","eran","estar","está","están","estaba",
        "estaban","tener","tiene","tienen","tuvo","tenía","haber","ha","han","había","hacer",
        "hace","hacen","hizo","hacía","poder","puede","pueden","pudo","podía","querer","quiere",
        "quieren","quiso","quería","decir","dice","dicen","dijo","decía","ir","va","van","fue",
        "iba","saber","sabe","saben","supo","sabía","bueno","buena","buenos","buenas","bien",
        "mal","malo","grande","gran","pequeño","vale","venga","vamos","está","ahí","allí","aquí",
        "sí","no","claro","verdad","hombre","mujer","chico","chica","vale","oiga","oye","mira",
        "mire","eso","esto","qué","cómo","cuándo","dónde","por","qué","ah","eh","oh","uy","bueno",
    },
    "fr": {
        "le","la","les","un","une","des","du","de","d'","et","ou","mais","si","dans","sur","sous",
        "avec","sans","pour","par","en","au","aux","ce","cette","ces","celui","celle","ceux",
        "qui","que","quoi","dont","où","quand","comment","pourquoi","parce","car","puisque",
        "je","tu","il","elle","on","nous","vous","ils","elles","me","te","se","lui","leur","y",
        "mon","ma","mes","ton","ta","tes","son","sa","ses","notre","nos","votre","vos","leur",
        "leurs","ce","cet","cette","ces","être","suis","es","est","sont","était","étaient","avoir",
        "ai","as","a","ont","avait","avaient","faire","fais","fait","font","faisait","faisaient",
        "aller","vais","vas","va","vont","allait","pouvoir","peux","peut","peuvent","voulais",
        "vouloir","veux","veut","veulent","savoir","sais","sait","savent","dire","dis","dit",
        "disent","plus","moins","très","bien","mal","beaucoup","peu","tout","tous","toute","toutes",
        "rien","quelque","quelques","autre","autres","même","mêmes","tellement","aussi","encore",
        "déjà","toujours","jamais","souvent","parfois","ici","là","maintenant","aujourd'hui",
        "oui","non","vraiment","bien sûr","d'accord","allez","voilà","tiens","bon","ok","hein",
        "ah","oh","ça","ben","quoi","voyons","voyez","regardez","monsieur","madame","mademoiselle",
    },
    "de": {
        "der","die","das","den","dem","des","ein","eine","einen","einem","einer","eines","und",
        "oder","aber","wenn","dann","von","zu","in","an","auf","mit","bei","nach","aus","über",
        "unter","vor","zwischen","durch","ohne","um","für","als","wie","so","sehr","mehr","schon",
        "noch","immer","wieder","dies","das","jener","solch","wer","was","wo","wann","warum","wie",
        "ich","du","er","sie","es","wir","ihr","Sie","mich","dich","sich","uns","euch","mir",
        "dir","ihm","ihr","ihnen","mein","dein","sein","unser","euer","ihr","sein","sein","haben",
        "hat","hatten","sein","ist","sind","war","waren","werden","wird","wurde","wurden","können",
        "kann","konnte","wollen","will","wollte","müssen","muss","musste","sollen","soll","sollte",
        "dürfen","darf","mögen","mag","mochte","tun","machen","hat","gemacht","sagen","sagt",
        "gesagt","sehen","sieht","gesehen","kommen","kommt","gekommen","gehen","geht","gegangen",
        "gut","schlecht","groß","klein","schön","neu","alt","ja","nein","nicht","kein","keine",
        "auch","nur","schon","noch","wieder","immer","sehr","wirklich","vielleicht","vielleicht",
        "natürlich","klar","also","doch","mal","halt","eben","schon","eigentlich","ungefähr",
        "Herr","Frau","Fräulein","bitte","danke","entschuldigung","Hallo","Tsüss","na","ach","oh",
    },
    "it": {
        "il","lo","la","i","gli","le","un","uno","una","di","a","da","in","con","su","per","tra",
        "fra","e","o","ma","se","perché","quando","come","dove","chi","che","cosa","quale",
        "io","tu","lui","lei","noi","voi","loro","mi","ti","si","ci","vi","me","te","sé","mio",
        "mia","tuo","tua","suo","sua","nostro","vostro","essere","sono","sei","è","siamo","siete",
        "era","erano","essere","stato","stata","avere","ho","hai","ha","abbiamo","avete","hanno",
        "aveva","avevano","fare","faccio","fai","fa","facciamo","fate","fanno","faceva","andare",
        "vado","va","vanno","andava","potere","posso","puoi","può","possiamo","potete","possono",
        "volete","volere","voglio","vuoi","vuole","vogliamo","volete","vogliono","dire","dico",
        "dici","dice","diciamo","dite","dicono","bene","male","molto","poco","tanto","tutto",
        "tutti","tutte","niente","nulla","qualcosa","qualcuno","anche","solo","sempre","mai",
        "già","ancora","ora","adesso","qui","lì","là","sì","no","forse","davvero","certo","cioè",
        "allora","dunque","insomma","mah","boh","ah","oh","eh","beh","prego","grazie","scusa",
        "ciao","arrivederci","signore","signora","signorina","bravo","brava","bene","dai","su",
    },
    "pt": {
        "o","a","os","as","um","uma","uns","umas","de","do","da","dos","das","em","no","na","nos",
        "nas","por","para","com","sem","sob","sobre","entre","até","desde","como","e","ou","mas",
        "se","porque","quando","onde","como","quem","que","qual","quais","eu","tu","ele","ela",
        "nós","vós","eles","elas","você","vocês","me","te","se","nos","vos","lhe","lhes","meu",
        "minha","teu","tua","seu","sua","nosso","vossa","dele","dela","ser","sou","és","é","somos",
        "são","era","eram","será","serão","estar","estou","está","estamos","estão","estava",
        "estavam","ter","tenho","tem","temos","têm","tinha","tinham","ir","vou","vai","vamos",
        "vão","ia","iam","fazer","faço","faz","fazemos","fazem","fiz","fez","faria","poder","posso",
        "pode","podem","pude","querer","quero","quer","querem","quis","saber","sei","sabe","sabem",
        "dizer","digo","diz","dizem","disse","bom","boa","mau","má","grande","pequeno","muito",
        "pouco","tudo","nada","algo","alguém","ninguém","também","só","sempre","nunca","ainda",
        "já","agora","aqui","aí","ali","sim","não","talvez","realmente","claro","então","mas","né",
        "oi","olá","tchau","obrigado","obrigada","de","nada","por","favor","bem","vamos","vir",
        "certo","sr","sra","srta","seu","ilha","pessoal","gente","coisa","coisas","assim","tipo",
    },
}


# ---------------------------------------------------------------------------
# Subtitle parsing
# ---------------------------------------------------------------------------

def parse_srt(content):
    """Parse SRT subtitle content into a list of (index, start, end, text) tuples."""
    blocks = re.split(r'\n\s*\n', content.strip())
    subtitles = []
    for block in blocks:
        lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
        if len(lines) < 2:
            continue
        # Try to parse index
        idx = 0
        time_line_idx = 0
        if lines[0].isdigit():
            idx = int(lines[0])
            time_line_idx = 1
        if time_line_idx >= len(lines):
            continue
        time_match = re.match(
            r'(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})',
            lines[time_line_idx]
        )
        if not time_match:
            continue
        start, end = time_match.groups()
        text = ' '.join(lines[time_line_idx + 1:])
        # Clean HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Clean ASS/SSA overrides
        text = re.sub(r'\{[^}]+\}', '', text)
        subtitles.append((idx, start, end, text))
    return subtitles


def parse_vtt(content):
    """Parse WebVTT subtitle content."""
    if content.startswith('WEBVTT'):
        content = content[6:]
    # Normalize VTT timestamps to SRT format (replace . with ,)
    content = re.sub(r'(\d{2}:\d{2}:\d{2})\.(\d{3})', r'\1,\2', content)
    return parse_srt(content)


def parse_subtitle_file(filepath):
    """Parse any supported subtitle file."""
    ext = Path(filepath).suffix.lower()
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if ext == '.srt':
        return parse_srt(content)
    elif ext == '.vtt':
        return parse_vtt(content)
    elif ext == '.txt':
        return [(0, '', '', line.strip()) for line in content.split('\n') if line.strip()]
    else:
        # Try SRT as fallback
        return parse_srt(content)


# ---------------------------------------------------------------------------
# Tokenization & analysis
# ---------------------------------------------------------------------------

def tokenize(text, language='en'):
    """Tokenize text into lowercase words, removing punctuation."""
    # Handle apostrophes based on language
    text = text.lower()
    # Keep apostrophes for contractions (English: don't, French: l'après)
    words = re.findall(r"[a-zà-ÿ\-'’]+", text)
    return [w.strip("'-") for w in words if w.strip("'-")]


def analyze_subtitles(subtitles, language='en'):
    """Analyze subtitles: word frequencies, sentences, phrases."""
    stop_words = STOP_WORDS.get(language, set())

    all_text = ' '.join(s[3] for s in subtitles)
    sentences = [s[3] for s in subtitles]

    words = tokenize(all_text, language)
    total_tokens = len(words)
    word_freq = Counter(words)

    # Content words (filter stop words)
    content_words = {w: c for w, c in word_freq.items() if w not in stop_words and len(w) >= 2}
    content_freq = Counter(content_words)

    # Bigram extraction (common two-word phrases)
    bigrams = Counter()
    for sent in sentences:
        toks = tokenize(sent, language)
        for i in range(len(toks) - 1):
            bg = (toks[i], toks[i + 1])
            if bg[0] not in stop_words and bg[1] not in stop_words:
                bigrams[bg] += 1

    # Trigram extraction
    trigrams = Counter()
    for sent in sentences:
        toks = tokenize(sent, language)
        for i in range(len(toks) - 2):
            tg = (toks[i], toks[i + 1], toks[i + 2])
            trigrams[tg] += 1

    return {
        "language": language,
        "total_subtitles": len(subtitles),
        "total_words": total_tokens,
        "unique_words": len(word_freq),
        "unique_content_words": len(content_freq),
        "word_freq": word_freq,
        "content_freq": content_freq,
        "bigrams": bigrams,
        "trigrams": trigrams,
        "sentences": sentences,
    }


def estimate_cefr(rank):
    """Estimate CEFR level based on frequency rank."""
    if rank <= 100:
        return "A1"
    elif rank <= 500:
        return "A2"
    elif rank <= 1500:
        return "B1"
    elif rank <= 4000:
        return "B2"
    elif rank <= 10000:
        return "C1"
    else:
        return "C2"


def find_context_sentence(word, sentences, max_context=1):
    """Find the first sentence containing the word for context."""
    contexts = []
    for sent in sentences:
        toks = set(tokenize(sent))
        if word in toks:
            contexts.append(sent)
            if len(contexts) >= max_context:
                break
    return contexts[0] if contexts else ""


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_analyze(args):
    subs = parse_subtitle_file(args.file)
    analysis = analyze_subtitles(subs, args.language)

    print("=" * 60)
    print(f"  SUBTITLE ANALYSIS — {os.path.basename(args.file)}")
    print(f"  Language: {args.language} | Subtitles: {analysis['total_subtitles']}")
    print("=" * 60)
    print(f"  Total words:        {analysis['total_words']:,}")
    print(f"  Unique words:       {analysis['unique_words']:,}")
    print(f"  Content words:      {analysis['unique_content_words']:,} (after stopword removal)")
    print()

    print("  TOP 30 CONTENT WORDS:")
    print("  " + "-" * 56)
    for rank, (word, count) in enumerate(analysis['content_freq'].most_common(30), 1):
        cefr = estimate_cefr(rank)
        bar = "█" * min(count, 30)
        print(f"  {rank:>3}. {word:<20} {count:>4}x  [{cefr}]  {bar}")
    print()

    print("  TOP 15 PHRASES (bigrams):")
    for rank, ((w1, w2), count) in enumerate(analysis['bigrams'].most_common(15), 1):
        if count >= 2:
            print(f"  {rank:>3}. {w1} {w2:<25} {count:>3}x")
    print()

    # Coverage analysis
    total = analysis['total_words']
    cumulative = 0
    print("  VOCABULARY COVERAGE:")
    for target in [100, 200, 500, 1000, 2000]:
        if target > analysis['unique_content_words']:
            break
        top_words = [w for w, _ in analysis['content_freq'].most_common(target)]
        coverage = sum(analysis['word_freq'].get(w, 0) for w in top_words) / total * 100 if total else 0
        print(f"    Top {target:>5} content words → {coverage:.1f}% coverage")
    print()


def cmd_build_season(args):
    """Build combined frequency list from multiple subtitle files."""
    sub_files = sorted(glob_subtitles(args.directory))
    if not sub_files:
        print(f"No subtitle files found in {args.directory}")
        sys.exit(1)

    print(f"Processing {len(sub_files)} subtitle files...")
    combined_words = Counter()
    combined_content = Counter()
    combined_bigrams = Counter()
    all_sentences = []
    file_stats = []

    for f in sub_files:
        subs = parse_subtitle_file(f)
        analysis = analyze_subtitles(subs, args.language)
        combined_words += analysis['word_freq']
        combined_content += analysis['content_freq']
        combined_bigrams += analysis['bigrams']
        all_sentences.extend(analysis['sentences'])
        file_stats.append({
            "file": os.path.basename(f),
            "subtitles": analysis['total_subtitles'],
            "words": analysis['total_words'],
            "unique_content": analysis['unique_content_words'],
        })
        print(f"  ✓ {os.path.basename(f)} — {analysis['total_words']} words")

    deck = {
        "source": args.directory,
        "language": args.language,
        "files_processed": len(sub_files),
        "total_words": sum(combined_words.values()),
        "unique_words": len(combined_words),
        "unique_content_words": len(combined_content),
        "file_stats": file_stats,
        "top_words": [
            {
                "rank": i,
                "word": w,
                "count": c,
                "cefr": estimate_cefr(i),
                "context": find_context_sentence(w, all_sentences),
            }
            for i, (w, c) in enumerate(combined_content.most_common(args.top), 1)
        ],
        "top_phrases": [
            {"phrase": f"{w1} {w2}", "count": c}
            for (w1, w2), c in combined_bigrams.most_common(50) if c >= 3
        ],
    }

    output = args.output or os.path.join(args.directory, "season_deck.json")
    with open(output, 'w') as f:
        json.dump(deck, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"  SEASON DECK — {len(sub_files)} files")
    print(f"{'='*60}")
    print(f"  Total words:      {deck['total_words']:,}")
    print(f"  Unique words:     {deck['unique_words']:,}")
    print(f"  Content words:    {deck['unique_content_words']:,}")
    print(f"  Deck size:        {len(deck['top_words'])} cards")
    print(f"\n✓ Deck saved to {output}")


def cmd_export(args):
    """Export flashcard deck from subtitle file."""
    subs = parse_subtitle_file(args.file)
    analysis = analyze_subtitles(subs, args.language)

    cards = []
    for rank, (word, count) in enumerate(analysis['content_freq'].most_common(args.top), 1):
        context = find_context_sentence(word, analysis['sentences'])
        cards.append({
            "rank": rank,
            "word": word,
            "frequency": count,
            "cefr": estimate_cefr(rank),
            "context": context,
            "translation": "",  # Placeholder for user/LLM to fill
        })

    if args.format == 'json':
        output = args.output or args.file.rsplit('.', 1)[0] + '_deck.json'
        with open(output, 'w') as f:
            json.dump(cards, f, indent=2, ensure_ascii=False)
    elif args.format == 'csv':
        output = args.output or args.file.rsplit('.', 1)[0] + '_deck.csv'
        with open(output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['rank', 'word', 'frequency', 'cefr', 'context', 'translation'])
            writer.writeheader()
            writer.writerows(cards)
    elif args.format == 'anki':
        # Anki TSV: front, back, context
        output = args.output or args.file.rsplit('.', 1)[0] + '_deck.tsv'
        with open(output, 'w') as f:
            f.write("#separator:tab\n")
            f.write("#html:false\n")
            f.write("Word\tFrequency\tCEFR\tContext Sentence\n")
            for c in cards:
                # Escape tabs/newlines in context
                ctx = c['context'].replace('\t', ' ').replace('\n', ' ')
                f.write(f"{c['word']}\t{c['frequency']}\t{c['cefr']}\t{ctx}\n")
    else:
        print(f"Unknown format: {args.format}")
        sys.exit(1)

    print(f"✓ Exported {len(cards)} cards to {output} (format: {args.format})")


def cmd_compare(args):
    """Compare vocabulary across multiple subtitle files."""
    sub_files = sorted(glob_subtitles(args.directory))
    if not sub_files:
        print(f"No subtitle files found in {args.directory}")
        sys.exit(1)

    print(f"Comparing {len(sub_files)} subtitle files...\n")
    word_in_files = defaultdict(set)
    word_total_freq = Counter()

    for f in sub_files:
        subs = parse_subtitle_file(f)
        analysis = analyze_subtitles(subs, args.language)
        fname = os.path.basename(f)
        for word, count in analysis['content_freq'].items():
            word_in_files[word].add(fname)
            word_total_freq[word] += count

    # Words appearing in most files (highest cross-episode value)
    cross_words = sorted(word_in_files.items(), key=lambda x: len(x[1]), reverse=True)

    print("=" * 70)
    print(f"  CROSS-FILE VOCABULARY — Top {args.top} by ubiquity")
    print("=" * 70)
    print(f"  {'Word':<20} {'In Files':>8} {'Total Freq':>12} {'CEFR'}")
    print("  " + "-" * 66)
    shown = 0
    for rank, (word, files) in enumerate(cross_words, 1):
        if shown >= args.top:
            break
        n_files = len(files)
        total = word_total_freq[word]
        cefr = estimate_cefr(rank)
        print(f"  {word:<20} {n_files:>5}/{len(sub_files):<2} {total:>10}x  [{cefr}]")
        shown += 1

    print(f"\n  Words appearing in ALL {len(sub_files)} files: ", end="")
    universal = [w for w, files in word_in_files.items() if len(files) == len(sub_files)]
    print(f"{len(universal)} words")


def glob_subtitles(directory):
    """Find all .srt, .vtt, .txt subtitle files in directory."""
    p = Path(directory)
    files = []
    for ext in ['*.srt', '*.vtt', '*.txt']:
        files.extend(str(f) for f in p.glob(ext))
    return files


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Language Immersion TV — extract vocabulary from subtitles.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    p_analyze = sub.add_parser("analyze", help="Analyze a single subtitle file")
    p_analyze.add_argument("file", help="Subtitle file (.srt, .vtt, .txt)")
    p_analyze.add_argument("--language", default="en", help="Language code (en, es, fr, de, it, pt)")

    p_build = sub.add_parser("build-season", help="Build combined deck from subtitle directory")
    p_build.add_argument("directory", help="Directory of subtitle files")
    p_build.add_argument("--language", default="en")
    p_build.add_argument("--output", help="Output JSON path")
    p_build.add_argument("--top", type=int, default=200, help="Top N words to include (default 200)")

    p_export = sub.add_parser("export", help="Export flashcard deck")
    p_export.add_argument("file", help="Subtitle file")
    p_export.add_argument("--language", default="en")
    p_export.add_argument("--format", choices=['anki', 'csv', 'json'], default='anki')
    p_export.add_argument("--output", help="Output file path")
    p_export.add_argument("--top", type=int, default=200, help="Top N words to export (default 200)")

    p_compare = sub.add_parser("compare", help="Compare vocabulary across files")
    p_compare.add_argument("directory", help="Directory of subtitle files")
    p_compare.add_argument("--language", default="en")
    p_compare.add_argument("--top", type=int, default=100)

    args = parser.parse_args()

    if args.command == "analyze":
        cmd_analyze(args)
    elif args.command == "build-season":
        cmd_build_season(args)
    elif args.command == "export":
        cmd_export(args)
    elif args.command == "compare":
        cmd_compare(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
