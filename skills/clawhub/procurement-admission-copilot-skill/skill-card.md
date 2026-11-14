## Description:

Shadow-mode copilot for B2B procurement admission. Given a supplier's raw qualification inputs, it checks material-package completeness and internal consistency; given a set of approval cases, it tracks status, stalls, and gaps. It never drafts contract terms or makes the admission decision — only structures and flags for a human to decide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams use it to check supplier admission packages for missing documents and inconsistencies, or to track stalls and gaps across approval cases. It produces review material for a human committee or reviewer, who retains responsibility for procurement decisions.

### Deployment Geography for Use:

Global, with China-specific identity checks such as the Unified Social Credit Code (USCC).

## Known Risks and Mitigations:

Risk: The skill has no declared tool scope, and the security scan does not establish how the host runtime limits its file access.

Mitigation: Review the host's file permissions and use an environment that limits access to the intended procurement materials.

## Reference(s):

- [Qualification checklist](references/qualification-checklist.md)
- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/procurement-admission-copilot-skill)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured JSON checks and Markdown material-package, readiness, or case-dashboard reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only findings with P0/P1/P2 flags and recommended actions; human confirmation is required, and the skill does not make admission decisions or draft contract terms.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
