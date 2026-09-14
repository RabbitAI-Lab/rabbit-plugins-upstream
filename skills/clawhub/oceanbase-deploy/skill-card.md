## Description:

Route community and commercial distributed OceanBase deployment and operations through obd. Use for general or multi-domain OceanBase/obd requests, product-form discovery, or when the correct specialized skill is unclear. Route concrete work to cluster management, OBD administration, tenant management, testing, or diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oceanbase](https://clawhub.ai/user/oceanbase)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and database operators use this skill to plan, review, and execute OceanBase distributed deployment and operations through OBD, with routing for cluster management, OBD administration, tenant management, testing, and diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill can normalize persistent root SSH access changes and other privileged deployment actions.

Mitigation: Require explicit approval and target review before root SSH use, authorized_keys changes, package installation targets, autodeploy execution, or other persistent environment changes.

Risk: The security guidance identifies wildcard tenant allowlists and empty tenant passwords as unsafe defaults for production use.

Mitigation: For production tenant creation, supply a strong password and restricted allowlist instead of relying on default tenant creation behavior.

Risk: The security verdict is suspicious and recommends review before real-environment installation.

Mitigation: Pin the installer or repository revision, review the selected workflow before execution, and validate every high-impact operation against the resolved targets.

## Reference(s):

- [README](README.md)
- [Operation Contract](references/operation-contract.md)
- [Product and Capability Resolution](references/product-and-capability-resolution.md)
- [Deployment Package Closure](references/deployment-package-sets.md)
- [Completion Criteria](references/completion-criteria.md)
- [Failure Recovery and Evidence](references/failure-recovery-and-evidence.md)
- [Automation Execution](references/automation-execution.md)
- [OceanBase Public Mirror](https://mirrors.oceanbase.com)
- [Aliyun OceanBase Mirror](https://mirrors.aliyun.com/oceanbase)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution plans, command sequences, configuration drafts, verification steps, and operational risk notes.]

## Skill Version(s):

2.0.3 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
