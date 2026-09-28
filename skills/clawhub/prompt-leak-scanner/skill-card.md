## Description:

Scans prompts before sharing for secrets, internal paths, personal information, custom sensitive terms, and instructions that could expose a system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and prompt authors use this local scanner to check selected prompt files or text before publishing or sharing them. High-risk findings block the release; other findings warrant manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from a source you have not verified may introduce untrusted code.

Mitigation: Install only if you trust the GitHub or npx source.

Risk: Automated findings may be mistaken for definitive release decisions.

Mitigation: Scan only intentionally selected prompt files and review findings manually before blocking a release.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-leak-scanner)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON findings, Guidance]

**Output Format:** [Console text or JSON with finding categories, severity, positions, and samples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit status 1 for high-risk findings, 0 otherwise, and 2 for input errors; medium-risk findings require review.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
