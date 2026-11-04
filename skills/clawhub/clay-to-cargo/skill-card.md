## Description:

Guides teams through rebuilding a Clay enrichment table in Cargo by mapping columns to provider actions, pricing a sample run, checking parity, and keeping the resulting workflow as code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and RevOps teams use this skill to migrate an existing Clay enrichment table to Cargo, estimate costs on a bounded sample, compare results with Clay, and express the workflow as reviewable code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sample runs can send contact names, email addresses, company domains, or LinkedIn URLs to Cargo and selected providers, and can consume credits.

Mitigation: Use only records authorized for that processing. Begin with a 10–20 row sample, report the observed cost and fill rate, and get approval with the row count and credit estimate before a full run.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/clay-to-cargo)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [ClayMate Lite column schema exporter](https://github.com/GTM-Base/claymate-lite)
- [Complete Clay-to-Cargo migration recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/clay-to-cargo.md)
- [Cargo project skill](https://github.com/getcargohq/cargo-skills/blob/main/cargo-project/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline JSON and Bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: frontmatter; confirmed by release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
