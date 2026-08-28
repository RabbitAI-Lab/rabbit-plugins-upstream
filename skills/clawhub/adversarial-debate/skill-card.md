## Description:

Cross-vendor adversarial review for plans, proposals, or designs, using an external attacker model, defender rulings, and a final consensus round.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and reviewers use this skill when they explicitly want an external model to challenge a plan, proposal, or design before acting on it. It helps produce ranked objections, defender rulings, consensus items, and open disagreements for the user to confirm.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review briefs and debate outputs may be stored locally during the workflow.

Mitigation: Delete generated brief, attack, defense, result, and judge files when the review is complete.

Risk: Review briefs may be sent to configured external model providers.

Mitigation: Redact secrets, personal data, regulated content, and proprietary details that are not necessary for the review before invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/adversarial-debate)
- [Publisher profile](https://clawhub.ai/user/xiaoba-dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with optional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local markdown brief, attack, defense, result, and judge files during a debate; no decision is final until the main session returns it to the user for confirmation.]

## Skill Version(s):

2.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
