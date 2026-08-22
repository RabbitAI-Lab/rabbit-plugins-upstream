## Description:

Review and fix AI-generated or AI-translated Arabic so it reads as fluent, native Modern Standard Arabic (MSA) instead of translated/calqued output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content teams use this skill to translate into Arabic, write Arabic prose, or review Arabic text for fluent MSA. It checks Latin-script leakage, calqued structure, terminology, morphology, punctuation, hamza spelling, dialectal leakage, and register before final output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate automatically for longer Arabic output.

Mitigation: Review generated Arabic and checklist findings before publishing or sending final text.

Risk: The skill may update local glossary, register profile, and failure-log notes.

Mitigation: Review those local reference files when tighter control over tone preferences, terminology, or learned correction patterns is required.

## Reference(s):

- [QALB Guidelines v0.90](http://nlp.qatar.cmu.edu/qalb/QALB-guidelines_0.90.pdf)
- [Fasaha Checklist](references/checklist.md)
- [QALB Spelling & Punctuation Reference](references/qalb-spelling-rules.md)
- [Worked Machine Translation Correction Examples](references/mt-examples.md)
- [Dialect Classification Reference](references/dialect-classification.md)
- [Arabic Voice & Register Profile](references/voice-profile.md)
- [Arabic Terminology Glossary](references/terminology.md)
- [LLM Arabic Failure Log](references/llm-failure-log.md)
- [Source Bibliography](references/sources.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with revised Arabic text, checklist findings, and correction notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local glossary, register profile, and failure log when new terminology or patterns are identified.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
