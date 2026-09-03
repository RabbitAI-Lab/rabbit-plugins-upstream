## Description:

Creates restrained Chinese narrative prose in a cold first-person style that uses concrete numbers, objects, spare dialogue, and anticlimactic endings while requiring fictionalized people, institutions, and events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT-0

## Use Case:

External writers and agents use this skill to draft or revise fictional Chinese self-narrative essays with a deliberately restrained, deadpan style. It is intended for personal narrative, social-media longform, and fictional documentary-style prose rather than speeches, marketing copy, academic writing, or poetry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may request prose about real people, real institutions, or sensitive allegations.

Mitigation: Replace identifiable details with fictional names and entities before writing; refuse if the user insists on using real identifiable subjects.

Risk: The style fingerprint is based on one anonymized source text, which can overfit and transfer poorly to other forms.

Mitigation: Use the style primarily for fictional first-person self-narrative; disclose lower confidence for third-person, advertising, speeches, academic writing, or low-tension topics.

Risk: Revision requests such as making the prose more emotional or more polished can cause style drift.

Mitigation: Apply only local parameter adjustments such as added silence beats, precise objects, or one functional cold metaphor, while preserving zero emotional adjectives and the deadpan structure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qomob/skills/justin-writing-style)
- [Style Fingerprint](artifact/references/style.md)
- [Creative Principles](artifact/references/principles.md)
- [Runtime Judge, Critique, and Revision Loop](artifact/references/runtime.md)
- [Anti-Patterns](artifact/references/anti-patterns.md)
- [Output Template and Safety Contract](artifact/templates/output.md)
- [Honest Boundaries](artifact/honest-boundaries.md)
- [Evaluation Suite](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text Chinese narrative prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs must use fictionalized names, institutions, and events; the skill may provide localized critique or revision guidance when evaluating drafts.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter and changelog list 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
