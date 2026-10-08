## Description:

A bilingual academic writing toolkit that checks style, cleans up drafts, and guides revisions while guarding terminology, citations, and numerical details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and editors use this skill to self-check Chinese or English academic drafts, revise stiff prose, and verify that critical terms, identifiers, and numbers survive editing. Style scores are writing heuristics, not evidence of authorship.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A rewrite may change a claim or omit a protected number, identifier, or technical term.

Mitigation: Review each rewrite against the original and run the integrity checks before using it.

Risk: A low style score could be mistaken for proof of human authorship or used to avoid required AI-use disclosure.

Mitigation: Treat scores only as writing feedback and retain any disclosure required by the relevant institution or publisher.

Risk: Learned term guards persist locally in the skill directory.

Mitigation: Review stored guards and remove them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Best practices](references/best_practices.md)
- [Compliance and disclosure guidance](references/compliance.md)
- [Programmatic usage](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, CSV, Guidance]

**Output Format:** [Revised text, revision guidance, and local style or integrity reports in plain text, Markdown, JSON, HTML, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally without network access; integrity checks compare protected details against the original draft.]

## Skill Version(s):

2.9.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
