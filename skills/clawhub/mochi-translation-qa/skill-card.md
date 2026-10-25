## Description:

Translate or polish user-provided text with the current model, then check bilingual segment alignment, required terminology, numbers and links and export a comparison with review issues. Use for 翻译校对, translation reviews or bilingual delivery; mechanical checks do not certify meaning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Translators, editors, and bilingual teams use the skill to translate or polish text and review existing translations. It compares aligned segments and flags terminology, number, and link mismatches for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mechanical checks do not establish that a translation preserves meaning, tone, negation, or context.

Mitigation: Review the translation against the source before relying on or sharing it.

Risk: The configured model may process supplied text, and local reports retain that text.

Mitigation: Avoid submitting sensitive material unless the model privacy terms and workspace are appropriate for it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/hznetnewpower/skills/mochi-translation-qa)
- [MochiLab](https://mochilab.bz/)
- [Translation input and outputs](artifact/references/input.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV]

**Output Format:** [Translated or polished text with Markdown comparison and JSON/CSV review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports flag mechanical issues for human review; they do not certify semantic accuracy. Requires Node.js 24+.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
