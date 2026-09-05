## Description:

Russian text quality support for typography, info-style editing, editorial review, UX writing, business correspondence, and AI-text cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[talkstream](https://clawhub.ai/user/talkstream)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, writers, editors, and product teams use this skill to improve Russian-language text, apply Russian typography defaults, review grammar and punctuation, prepare UX or business copy, and score text quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation can change Russian punctuation, quote style, number formatting, or editorial tone in normal responses.

Mitigation: Use the skill when those Russian typography and editorial defaults are desired; disable implicit invocation or request exact preservation when fidelity to the original text matters.

Risk: A proofreading or editing task could accidentally alter user-owned or third-party text beyond the user's intent.

Mitigation: Return corrected text with a change summary for review, preserve quoted material and code blocks, and rewrite files only when the user explicitly asks.

## Reference(s):

- [ru-text homepage](https://ru-text.org)
- [ClawHub skill page](https://clawhub.ai/talkstream/skills/ru-text)
- [Sources and Attribution](references/sources.md)
- [Russian Typography Rules](references/typography.md)
- [Info-Style Methodology](references/info-style.md)
- [Russian Text Anti-Patterns](references/anti-patterns.md)
- [Scoring: text quality assessment](references/scoring.md)
- [UX-writing on Russian language](references/ux-writing.md)
- [Russian Business Writing Guide](references/business-writing.md)
- [Editorial: Grammar and Style](references/editorial-grammar.md)
- [Editorial: Punctuation](references/editorial-punctuation.md)
- [Addenda](references/addenda.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Plain text or Markdown with corrected Russian text, change notes, diagnostics, and scoring when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May apply Russian typography silently to Russian output; file rewrites are only appropriate when explicitly requested by the user.]

## Skill Version(s):

2.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
