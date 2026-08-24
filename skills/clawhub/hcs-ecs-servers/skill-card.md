## Description:

Queries Huawei Cloud ECS instance lists with optional region and status filters, returning instance names, IDs, status, IP addresses, and flavor details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud ECS instances during routine inventory checks, troubleshooting, and operational review. It is intended for read-only listing and filtering of ECS server details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically searches environment variables and .project-info JSON files for Huawei AK/SK credentials.

Mitigation: Install only where this credential discovery behavior is acceptable, and provide least-privilege read-only Huawei credentials.

Risk: The server security summary flags broad credential discovery as needing review before installation.

Mitigation: Review triggers and credential scope before production use, and keep invocation wording specific to Huawei ECS listing.

Risk: Dependencies are declared with lower bounds only.

Mitigation: Pin or constrain Python dependencies before production deployment.

## Reference(s):

- [Huawei Cloud ECS API Reference](references/api-reference.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Functional Test Report](references/test-report.md)
- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/hcs-ecs-servers)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text tables or JSON returned from shell commands, with Markdown guidance for setup and verification.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The list-servers command can filter by region, status, limit, and offset.]

## Skill Version(s):

0.2.0 (source: server release metadata; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
