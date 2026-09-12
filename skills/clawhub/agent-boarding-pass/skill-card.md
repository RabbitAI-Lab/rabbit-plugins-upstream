## Description:

Issues a verifiable boarding pass for an AI agent with identity, evidence hashes, an allowlist, and a time-to-live, then verifies the pass by recomputing its fingerprint and checking expiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to create a portable governance record for an AI agent before onboarding it into prompts, repositories, tickets, or team workflows. The record helps reviewers see the agent identity, evidence basis, allowed actions, and expiry window in one deterministic artifact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat generated boarding passes as cryptographic authorization credentials.

Mitigation: Use the passes as governance and audit aids unless trusted issuer signatures and stronger evidence validation are added.

Risk: The trust and installation model requires review before relying on the skill for agent permissions.

Mitigation: Install only from a reviewed, pinned source and review or scan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-boarding-pass)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON boarding pass files and plain-text verification status, with command-line usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic output; uses SHA-256 fingerprints and exit codes 0, 1, and 2.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter; release metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
