## Description:

Install, launch, configure, and verify the Aidenwu0209/dsh-Unlimited-OCR-Skill native DeepSeek Harness bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to install the Unlimited-OCR bundle into DeepSeek Harness, launch the local web UI, configure Baidu Cloud or a local provider, and verify the Settings panel before reporting setup status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup depends on a referenced GitHub plugin and DeepSeek Harness tooling that the user must trust before installation.

Mitigation: Confirm trust in the referenced plugin and tooling before installing or launching them.

Risk: API keys or provider credentials could be exposed if handled through ordinary settings, logs, or source files.

Mitigation: Use DSH Credentials for API keys and do not echo, log, or store secrets in ordinary settings or source files.

Risk: Unrelated privileged or system changes could expand the setup beyond the intended OCR plugin installation.

Mitigation: Do not approve sudo or unrelated system changes unless the need is separately understood.

## Reference(s):

- [DSH Unlimited-OCR Skill Repository](https://github.com/Aidenwu0209/dsh-Unlimited-OCR-Skill)
- [ClawHub Skill Page](https://clawhub.ai/aidenwu0209/skills/dsh-unlimited-ocr-skill-setup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and setup status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, commands, local web URL, provider status, and remaining user-supplied values.]

## Skill Version(s):

1.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
