## Description:

Creates Huawei Cloud agent skills through a six-phase workflow covering requirements analysis, CLI/SDK/API research, documentation generation, test preparation, detailed testing, cleanup, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to scaffold Huawei Cloud skills that package CLI, SDK, or REST API operations into reusable agent workflows with validation, testing, and reference documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install an external quality telemetry CLI into the user's local bin directory.

Mitigation: Inspect the installer before use, run in a controlled environment, and set SKILL_QUALITY_REPORT=0 when telemetry is not wanted.

Risk: The workflow can run credentialed Huawei Cloud tests and cloud commands.

Mitigation: Use dedicated least-privilege temporary Huawei Cloud credentials and avoid production projects until review is complete.

Risk: Security evidence flags installer verification and mutation-confirmation gaps.

Mitigation: Require human review before executing generated commands, especially mutating operations, and confirm cleanup steps after testing.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [IAM Policies](references/iam-policies.md)
- [Related Commands](references/related-commands.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON summaries, shell commands, and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate SKILL.md, references, scripts, templates, phase summary JSON files, validation commands, and cleanup guidance.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
