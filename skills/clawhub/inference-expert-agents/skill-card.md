## Description:

Turn an AI agent into an expert at inference: difficulty triage, deliberation budgets, self-consistency, claim-level verification, citation gates, judge ensembles, calibrated abstention, cost cascades, semantic caching, deep-research loops, agent memory, MCP exposure, eval regression gates, and answer certificates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to decide how much inference compute to spend, verify claims before delivery, calibrate abstention, control inference cost, and gate agent answers with reusable CLI checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that privacy documentation conflicts with outbound citation checks.

Mitigation: Review before installing, and avoid using citecheck.py with confidential or unpublished research metadata unless egress to public scholarly registries is acceptable.

Risk: The security review found that the published verification hash does not match the inspected SKILL.md file.

Mitigation: Verify installed files against trusted release evidence before deployment, and treat mismatched hashes as a release integrity issue.

Risk: The skill's checks provide advice and gating signals, not independent authorization for consequential actions.

Mitigation: Require human review for consequential decisions such as spending money, deleting data, shipping high-stakes answers, or promoting models.

## Reference(s):

- [Verified Grounding](references/verified-grounding.md)
- [Release Notes v3](references/release-notes-v3.md)
- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/inference-expert-agents)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with bash examples and JSON CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tools are stdlib-only Python CLIs; persistent state is opt-in via explicit database paths.]

## Skill Version(s):

3.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
