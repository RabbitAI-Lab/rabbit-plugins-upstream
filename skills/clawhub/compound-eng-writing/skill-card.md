## Description:

Prose editing, rewriting, and AI-tell auditing for human-facing copy, documentation, emails, PR descriptions, and publication text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and teams use this skill to edit human-facing prose, preserve author voice, audit drafts for AI-like patterns, and produce PR or publication-ready Markdown without taking posting authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewritten text may change factual meaning, remove useful nuance, or alter the writer's voice before publication.

Mitigation: Review corrected text against the original draft for meaning, voice preservation, grammar, and audience fit before publishing.

Risk: Detect mode findings could be mistaken for proof that AI wrote a draft.

Mitigation: Use detect mode only to list observable patterns and fixes; avoid scores or authorship verdicts.

Risk: Citation-artifact cleanup or tracking-parameter removal can affect links or references in publication drafts.

Mitigation: Confirm citation replacements and URL query-string changes before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing)
- [ia-writing specification](artifact/SPEC.md)
- [Two-phase audit workflow](artifact/references/audit-workflow.md)
- [Editing and voice](artifact/references/editing-and-voice.md)
- [Before/after examples](artifact/references/examples.md)
- [Language and patterns](artifact/references/language-and-patterns.md)
- [Extended phrase reference](artifact/references/phrases.md)
- [PR and MR description style](artifact/references/pr-descriptions.md)
- [Publication surfaces](artifact/references/publication-surfaces.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with optional audit findings and changelog]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include corrected text, concise material changes, quoted audit findings, and publication-surface guidance depending on the request.]

## Skill Version(s):

4.5.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
