## Description:

Pre-execution safety guardrails for autonomous agents that classify proposed actions by risk and return ALLOW, CONFIRM, or DENY decisions with audit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check proposed agent actions before execution, especially commands or workflows with side effects such as deletion, deployment, data upload, or payment. It helps agents pause for confirmation or deny high-risk actions before irreversible changes occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local usage history and preferences may be persisted by the bundled learner.

Mitigation: Review the learner behavior before installation and remove or disable it when local memory is not desired.

Risk: The learner encourages instruction changes over time, which can alter future skill behavior.

Mitigation: Keep guardrail rules fixed for unattended or safety-critical workflows, and require human review before accepting any suggested instruction changes.

Risk: The guardrail checker is limited and should not be treated as a complete safety boundary.

Mitigation: Use it as a pre-execution review aid and keep human confirmation for medium, high, and critical actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/safety-guardrails)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, Python helper code, shell commands, and JSON decision records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guardrail decisions include decision and note fields; the bundled learner may persist local usage history and preferences.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
