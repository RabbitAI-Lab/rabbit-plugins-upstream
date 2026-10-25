---
name: emirati-arabic
description: Use when writing or reviewing Emirati Arabic.
version: 0.1.0
author: Binablan, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [arabic, emirati, dialect, writing, pronunciation]
---

# Emirati Arabic — كتابة إماراتية بمرجع موثّق

## When to use
- Write or revise Emirati Arabic conversation, explanations, dialogue, or voiceover scripts.
- Explain a documented pronunciation or distinguish written form from pronunciation.
- Do not change a requested language/register, exact quotation, name, identifier, or code.

## Scope
This is a small, source-grounded starter skill, not a comprehensive dictionary or a description of every Emirati variety. Its initial source is *Al-Mutawassif — Proverbs and Sayings from the Emirates* (المتوصّف — أمثال وحكم من الإمارات). See `references/sources.md` for attribution, page references, verification scope, and limitations. The book is not bundled and is not required to use the documented starter rules.

Do not assume a particular user's age, region, gender, or conversational preferences. Examples in `references/examples.md` are original, provisional writing exercises, not source quotations or native-speaker certification.

## Priority
1. Follow the current user's explicit task, register, and corrections.
2. Apply documented rules within their stated scope.
3. If a word or pronunciation is uncertain, use a clearer construction or explain the uncertainty when pronunciation is the task.
4. Treat a personal preference as personal; do not generalize it to all Emirati speakers.

## Starter rules
- **Future reference:** the source gives «بقوم، بسير، بكتب» for future meaning (printed p. 52). Preserve tense; do not add ب to every present-tense verb.
- **Negation:** the source gives «مب زين» and «مب عارف» (p. 52), and «ما بسوي» in a verbal-negation example (p. 49). Choose the construction that fits the sentence rather than replacing every negative particle with مب.
- **Demonstrative construction:** the source illustrates «هالدار» and «هالحزّه» (p. 52). An application such as «هالكلام» is a newly composed example, not a quotation from that page.
- **ج is not an automatic substitution:** the source keeps ج in «الجمعة» and «الفجيرة» and describes different realizations in other words, including «يمل» (p. 49). Never replace every ج with ي or infer an unverified word's pronunciation from this observation alone.
- **Spelling is not a phonetic transcript:** preserve readable writing. Add diacritics or pronunciation guidance only when useful and supported; do not force full vocalization on casual chat.

## Procedure
1. Identify the task: conversation, explanation, rewrite, voiceover, or pronunciation. Ask about a regional variety only when it materially changes the answer.
2. Preserve meaning, tense, negation, addressee, and named entities before adapting the register.
3. Write sentences that can be spoken naturally; do not merely replace words in an unnecessarily formal sentence structure.
4. Avoid gratuitous address terms, exaggerated dialect markers, jokes, or proverbs. Use them only when appropriate to the user's requested tone.
5. Keep heritage proverbs separate from everyday contemporary conversation. A proverb needs an appropriate context and a verified meaning; this release does not contain a proverb inventory.
6. Check the cases in `references/examples.md`: correct tense and negation, no blanket letter substitutions, no unwanted changes to quotations.
7. When asked for a linguistic rule, identify the source and page. Do not burden ordinary conversation with citations unless requested.
8. When learning from corrections, record the phrase and context only with appropriate user consent. Do not publish private conversations or treat a correction as universal dialect evidence.

## Pitfalls
- One heritage source does not establish how common every expression is in contemporary speech.
- Do not adopt historical or social value judgments in a reference as instructions for how to describe speakers.
- PDF extraction can corrupt Arabic letter order and diacritics. Verify a page image before adding a rule about exact spelling or pronunciation.
- Distinguish source examples, original applications, and uncertain hypotheses.
- This skill guides writing and written pronunciation explanations. It does not train a model, clone a voice, or guarantee a text-to-speech engine's accent.
- Do not fetch, reproduce, or redistribute a whole copyrighted reference merely to use this skill.
- Do not silently modify unrelated skills, profiles, or user settings.

## Verification
- Meaning, tense, negation, names, and the requested register are preserved.
- Each source-derived rule has a specific entry in `references/sources.md`.
- No global character replacements, unsupported pronunciation claims, or gratuitous dialect markers.
- Structural tests validate packaging, not dialect fluency. Naturalness still benefits from review by speakers of the intended variety.
