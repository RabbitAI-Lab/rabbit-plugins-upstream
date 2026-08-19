## Description:

Prose editing, rewriting, and humanizing text for natural tone, plus audits that flag AI-style patterns without assigning authorship.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, engineers, and product teams use this skill to edit copy, documentation, emails, blog posts, and PR or MR descriptions into clearer prose. They can also use detect mode to audit a draft for specific AI-style patterns before deciding whether to rewrite it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opinionated rewriting can change tone, meaning, or the author's recognizable voice.

Mitigation: Review the corrected text and changelog before publishing, especially for legal, executive, or customer-facing prose.

Risk: Audit findings can be misread as proof that AI wrote a draft.

Mitigation: Use detect-mode findings as reviewable pattern evidence only, and avoid presenting them as an authorship verdict.

Risk: Mechanical application of banned-phrase and formatting rules can remove useful technical detail.

Mitigation: Check edits against the source intent and preserve factual claims, examples, commands, and version-specific details.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [ia-writing specification](artifact/SPEC.md)
- [Two-phase audit workflow](artifact/references/audit-workflow.md)
- [Extended phrase reference](artifact/references/phrases.md)
- [Before/after examples](artifact/references/examples.md)
- [PR and MR description style](artifact/references/pr-descriptions.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-writing)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown prose with audit findings, corrected text, and changelog sections when rewriting is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detect mode reports pattern evidence without an authorship verdict; edit mode preserves the writer's voice while applying prose changes.]

## Skill Version(s):

4.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
