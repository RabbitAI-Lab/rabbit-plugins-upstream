## Description:

Fact Check Guard helps an agent treat key factual claims as claims to be proven, compare them with supplied sources, and label each claim as supported, dubious, or unsourced before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, editors, and agent operators use this skill to review AI-generated articles, reports, support replies, and other externally published content for source-backed factual claims. It is intended as a publication gate, not a replacement for expert judgment or regulated professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global or unpinned installation can make the skill available across agent sessions without a fixed reviewed version.

Mitigation: Review or pin the installer and repository version before installation, and avoid global installation unless broad availability is intended.

Risk: The fact-checking logic can create misplaced confidence because source matching is only a rough aid and does not prove a claim is true.

Mitigation: Keep human review and authoritative sources in the publication workflow, especially for sensitive, regulated, or high-impact claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/fact-check-guard)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance and optional JSON or text claim-check results from the bundled CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Labels claims as supported, dubious, or unsourced; CLI exits with rc=0 for pass, rc=1 for issues, and rc=2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
