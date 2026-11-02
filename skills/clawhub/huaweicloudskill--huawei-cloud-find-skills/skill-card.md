## Description:

Search, browse, view, and install Huawei Cloud agent skills from public Huawei Cloud skill indexes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to discover Huawei Cloud skills by keyword or category, review matching skill details, and install selected skills for later execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses default-on anonymous telemetry and may install persistent telemetry tooling in the user's environment.

Mitigation: Review the telemetry behavior before use and set SKILL_QUALITY_REPORT=0 if telemetry is not acceptable.

Risk: The skill can guide remote installation of additional Huawei Cloud skills through npx commands.

Mitigation: Review the matched skill and installation command before allowing installation.

Risk: The security verdict is suspicious because telemetry tooling and broad remote install commands deserve review before use.

Mitigation: Scan and review the skill before deployment, especially in restricted or enterprise environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-find-skills)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install additional Huawei Cloud skills through remote package commands when the user chooses a result.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
