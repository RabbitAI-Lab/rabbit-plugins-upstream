## Description:

Execute tasks with reliability-first behavior under flaky conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to decide when to retry transient failures, when to switch tactics, and when to escalate medium- or high-risk actions for confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic retries can repeat an operation that has side effects if the risk class is misjudged.

Mitigation: Limit automatic retries to low-risk, reversible or idempotent failures; notify for medium-risk actions and ask before high-risk actions.

Risk: Unclear blast radius can make a retry unsafe.

Mitigation: Treat uncertainty as medium risk, provide a brief mitigation or rollback path, and escalate before destructive, security-sensitive, or irreversible actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pinguy/skills/risk-aware-retry)
- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/risk-aware-retry)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown with concise status updates and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DONE or BLOCKED status, proof, risk notes, retry details, and next steps.]

## Skill Version(s):

0.1.0 (source: server release evidence; provenance commit 162736a1102855660a17be3daebd14537dbeacbf)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
