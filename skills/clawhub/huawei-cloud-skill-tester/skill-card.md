## Description:

End-to-end functional testing framework for Huawei Cloud skills with a three-tier pipeline for unit testing, multi-skill orchestration, real-environment execution, cleanup, and consolidated reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to test Huawei Cloud agent skills through installation checks, functional analysis, test case generation, live execution, orchestration scenarios, and final reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can touch real Huawei Cloud resources with inherited cloud credentials.

Mitigation: Run it only with a disposable, least-privilege Huawei Cloud account and keep write execution disabled unless each generated command has been reviewed.

Risk: The skill can install an unverified local executable before running quality telemetry.

Mitigation: Inspect the skill-quality-cli download source before installation and prefer an isolated environment for evaluation.

Risk: Sibling auto-scanning can broaden the set of skills included in orchestration tests.

Mitigation: Use --no-siblings or a low sibling limit when testing scope must stay narrow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-skill-tester)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Agent Protocol](references/agent-protocol.md)
- [Architecture](references/architecture.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Output Schema Specification](references/output-schema-spec.md)
- [Phase Details](references/phase-details.md)
- [Phase Transition Rules](references/phase-transition-rules.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated JSON/Markdown test reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase summary JSON files and timestamped final reports in a sibling test-files directory.]

## Skill Version(s):

1.0.3 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
