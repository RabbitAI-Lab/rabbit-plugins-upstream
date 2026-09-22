## Description:

Guides an AI agent through Huawei Cloud OptVerse workflows for mathematical programming, including requirement analysis, modeling, data checks, solving, report generation, asset publishing, and optional deployment and testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, optimization practitioners, and business analysts use this skill to run OptVerse decision-engine workflows for operations-research problems such as facility location, routing, and production scheduling. It helps the agent manage multi-round cloud interactions, artifacts, confirmations, publishing, and optional service testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles cloud credentials and business files while the security evidence reports unsafe TLS settings.

Mitigation: Use only in a controlled environment with data approved for Huawei Cloud processing, avoid untrusted networks until TLS verification is fixed, and ask the publisher to remove verify=False and skipSecureVerify guidance.

Risk: The security evidence reports under-disclosed token persistence and temp-file token-cache behavior.

Mitigation: Ask the publisher to remove or harden the temp-file token cache, align documentation with actual credential storage behavior, and rotate credentials or tokens if this version was used on an untrusted network or shared machine.

Risk: Automatic confirmation can bypass human review of intermediate optimization artifacts.

Mitigation: Do not use --auto-confirm on real workflows; review generated artifacts and confirm each stage deliberately before publishing or deploying an asset.

## Reference(s):

- [API Reference](references/api-reference.md)
- [Workflow Design](references/workflow-design.md)
- [Best Practices & Notes](references/best-practices.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [IAM Policies - OptVerse Solver Assistant](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Example Workflow](demo/example-workflow.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with shell commands, Python script usage, JSON request examples, and generated workflow artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and manages OptVerse artifacts such as requirement analysis, model code and documentation, data templates, solver outputs, reports, published asset IDs, and optional service test results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
