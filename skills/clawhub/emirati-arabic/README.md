# Emirati Arabic Skill | مهارة اللهجة الإماراتية

**By Binablan · v0.1.0 · MIT (original project material)**

مهارة أولية تساعد المساعدات الذكية على كتابة ومراجعة العربية الإماراتية، مع قواعد محدودة موثّقة وأمثلة قابلة للمراجعة. ليست معجمًا شاملًا، ولا بديلًا عن مراجعة متحدثي اللهجة.

A small, source-grounded skill for writing and reviewing Emirati Arabic. It prioritizes preserving meaning, avoiding mechanical letter substitutions, and distinguishing source evidence from original examples.

## Install in Hermes

```sh
hermes skills install https://raw.githubusercontent.com/Binablan/emirati-arabic/main/SKILL.md
```

For a compatible agent that supports `SKILL.md`, download the repository and follow that agent's skill-installation instructions. Compatibility with every agent has not been tested.

## Usage | الاستخدام

Ask your assistant, for example:

- «استخدم مهارة emirati-arabic وراجع هالنص، بدون ما تغيّر معناه.»
- «حوّل النص إلى كلام إماراتي بسيط، بدون مبالغة أو حشو أمثال.»
- «اشرح القاعدة الموجودة في المهارة، واذكر مصدرها.»

Original provisional example — not a source quotation:

> سوف أكتب لك الشرح. → بكتب لك الشرح.

The skill is guidance loaded by the assistant, not a new model, a voice, or an automatic guarantee of accent accuracy.

## What v0.1.0 covers

- Selected future, negation, and demonstrative constructions.
- A safeguard against indiscriminate ج → ي substitution.
- Meaning-preserving rewriting and restrained dialect markers.
- Source attribution, uncertainty, and private-versus-public correction handling.

## Reference and limitations

The initial reference is **«المتوصّف — أمثال وحكم من الإمارات»**, collected and researched by **عبدالله حمدان عبدالله أحمد بن دلموك**, published by **مركز حمدان بن محمد لإحياء التراث**, second edition, 2021 as stated in the examined copy.

The initial pronunciation/spelling rules were checked against images of printed pages **49 and 52**. This is not a claim that the whole book was reviewed. See [source notes](references/sources.md).

**The PDF, page images, bulk extracted text, private conversations, personal preferences, and local-machine files are not included.** This project is independent and does not claim endorsement by the author, publisher, or Nous Research.

## Contribute | المساهمة

Corrections and additional well-supported examples are welcome. Explain the context and, where relevant, the regional variety. Separate a personal preference from a broader claim. Do not upload private conversations or copyrighted books. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Tests

From the repository directory, with Python 3.10 or later:

```sh
python -m unittest discover -s tests -v
```

These tests check structure, references, and publication hygiene. They do not prove linguistic fluency or universal naturalness.

## License

Original instructions, documentation, code, and newly authored examples are provided under the [MIT License](LICENSE), copyright Binablan. The referenced book and any third-party source material retain their own rights; this repository does not license or redistribute the book. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
