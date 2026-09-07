## Description:

Part of the Overpowered skill suite, Completion Audit helps agents independently determine whether a claimed task outcome is complete by reconstructing completion criteria and checking fresh evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and reviewers use this skill to audit whether an agent's claimed work is actually complete by deriving observable criteria and checking authoritative evidence before accepting delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit may require access to files, logs, test outputs, database state, or other authoritative evidence to substantiate completion.

Mitigation: Use only evidence available through the agent's existing permissions and report NOT PROVEN when required verification is unavailable.

Risk: Relying on a worker's narrative, generated file existence, or a successful command exit code can lead to premature completion claims.

Mitigation: Derive observable criteria from the original objective and inspect fresh evidence for each criterion before returning a verdict.

## Reference(s):

- [Overpowered skill suite](https://github.com/raguets/overpowered)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text audit report with a criterion, evidence, and status table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an overall PROVEN or NOT PROVEN verdict and any remaining work or missing evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
