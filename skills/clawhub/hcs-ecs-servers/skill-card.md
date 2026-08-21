## Description:

Lists Huawei Cloud ECS server instances within a region/project scope, with optional name and status filtering, and returns instance name, ID, status, availability zone, flavor, IP address, and timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inventory Huawei Cloud ECS instances and filter results by name or status for troubleshooting, auditing, or infrastructure reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live inventory calls require Huawei Cloud AK/SK credentials and can expose cloud instance metadata to the execution environment.

Mitigation: Install only where ECS inventory access is intended, use least-privilege read-only credentials, and prefer mock mode for testing without cloud access.

Risk: The Huawei Cloud SDK dependencies are specified with lower bounds rather than exact pinned versions.

Mitigation: Review or pin SDK dependency versions before production deployment.

## Reference(s):

- [Huawei Cloud ECS API reference](references/ecs-servers-api.md)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/hcs-ecs-servers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; script output is JSON by default or a Markdown table when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live calls require Huawei Cloud AK/SK credentials; mock mode runs without cloud credentials.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
