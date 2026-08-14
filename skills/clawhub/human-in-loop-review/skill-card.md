## Description:

Routes risky, irreversible, privacy-sensitive, privileged, payment, and other side-effecting agent actions to a human review queue before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to add manual approval gates to autonomous agents or automated pipelines before medium, high, critical, irreversible, privileged, external, payment, deletion, deployment, or shutdown actions proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI review queue is memory-backed, so approvals and pending items are not preserved between separate command runs.

Mitigation: Add durable queue storage and test restart behavior before relying on the skill for operational approvals.

Risk: The bundled learning module persists usage history and preferences, and the skill text describes automatic modification of SKILL.md.

Mitigation: Make learning opt-in, document storage permissions and retention, and prohibit automatic skill-file modification unless a human explicitly approves the change.

Risk: Server security evidence marks the release as suspicious pending production hardening.

Mitigation: Treat the skill as a review-bucket component requiring changes before production use, then rescan and re-review before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/human-in-loop-review)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Python CLI commands and JSON review records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pending, approved, rejected, and summary review data; CLI queue state is not durable between separate runs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
