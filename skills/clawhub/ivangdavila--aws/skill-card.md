## Description:

Architects, debugs, secures, and cost-optimizes AWS infrastructure across EC2, Lambda, RDS, VPC, IAM, ECS, CloudFront, infrastructure as code, accounts, reliability, and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and cloud engineers use this skill to plan, troubleshoot, harden, operate, and cost-review AWS environments. It is especially suited for AWS CLI-driven diagnosis, service selection, IAM and network review, billing investigation, and production readiness work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS CLI actions can affect resources through the user's configured AWS identity, including account changes when create, modify, delete, terminate, force, S3 sync, or IAM-related commands are approved.

Mitigation: Review commands before allowing account changes and require explicit confirmation for destructive or privilege-sensitive operations.

Risk: The skill maintains local operational notes that can include account IDs, resource names, spend history, and generated runbooks.

Mitigation: Keep ~/Clawic/data/ under the user's control, avoid sharing those notes without review, and store only credential pointers rather than secret values.

Risk: Cloud guidance can become inaccurate if it uses stale inventory, an unintended profile, or the wrong region.

Mitigation: Confirm the AWS identity and region before material changes, read stored inventory first, and verify live account state and current pricing before committing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/aws)
- [Clawic skill homepage](https://clawic.com/skills/aws)
- [Skill definition](artifact/SKILL.md)
- [Security guide](artifact/security.md)
- [CLI toolkit](artifact/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with AWS CLI commands, infrastructure and policy snippets, runbook text, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local note updates under ~/Clawic/data/ and AWS CLI actions using the user's configured AWS identity.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
