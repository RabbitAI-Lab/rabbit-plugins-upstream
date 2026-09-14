## Description:

Agent Kill Switch helps developers create and check pre-deployment kill-switch cards that define stop conditions, privilege revocation actions, responsible owners, and recovery criteria for AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill before deploying AI agents to produce a kill-switch card and to validate that required launch-blocking fields are present.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote installation can fetch changed content into persistent skill directories.

Mitigation: Review the installation path and prefer a pinned release, tag, commit, or verified checksum before installing.

Risk: A complete kill-switch card is a governance aid, not a substitute for professional, legal, or operational approval.

Mitigation: Require human review for regulated, high-impact, or cross-team deployment decisions before launch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-kill-switch)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with CLI examples and JSON kill-switch card output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script exits with rc=0 for success, rc=1 for incomplete cards, and rc=2 for usage or unreadable-input errors.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
