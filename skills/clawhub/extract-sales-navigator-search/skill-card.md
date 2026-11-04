## Description:

Extract large Sales Navigator searches by counting results, splitting them under per-search caps, merging the pieces into fewer searches, and loading them into Cargo models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales operations, revenue operations, and GTM engineering teams use the skill to extract account or people searches larger than Sales Navigator's per-search limits and organize the results into Cargo models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full extractions can consume substantial Cargo credits, and people searches may require repeated runs.

Mitigation: Review the credit estimate before approval and validate the URLs with one small extraction before running the full set.

Risk: Using a personal Sales Navigator seat for searches can put that account at risk of restriction.

Mitigation: Run searches cookieless by default; use a personal seat only for seat-dependent filters and only after the user explicitly agrees.

Risk: The skill installs the Cargo CLI from a moving latest package tag, and optional additional skill packs are outside this artifact review.

Mitigation: Consider pinning dependency versions and review the additional skill pack separately before installing it.

## Reference(s):

- [Cargo GTM skills homepage (listed as the skill homepage)](https://github.com/getcargohq/gtm-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/extract-sales-navigator-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, JSON configuration examples, tables, and procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides instructions for counting and splitting account or people searches, creating Cargo models, checking extraction results, and deduplicating records.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
