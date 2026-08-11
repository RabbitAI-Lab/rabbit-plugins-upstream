## Description:

Provides bounded, read-only checks that compare supplied trace/link evidence and reconcile supplied evaluation-cost events for human-authorized review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[slowsleeper1](https://clawhub.ai/user/slowsleeper1)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and agents use this skill to assess supplied trace/link manifests and reconcile supplied trace-cost events within a read-only, human-authorized workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive or production data could be submitted to an unsuitable request path.

Mitigation: Do not provide secrets, credentials, customer data, or production traces unless a separate trusted process is established.

Risk: Users may overread the descriptor as an automated service or evidence of runtime capability.

Mitigation: Treat the skill as guidance for a human-authorized, supplied-evidence workflow; verify availability and authorization before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/slowsleeper1/skills/soja-trace-evidence-checks)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only findings for human review; no endpoint, installation, payment, telemetry, or automatic execution is available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
