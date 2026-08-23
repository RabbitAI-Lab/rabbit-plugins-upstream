## Description:

Signup and registration collection agent that prompts users for name, occupation, WeChat ID, and entrepreneurship experience, checks for duplicate WeChat IDs through a relay service, and submits new or updated records to a Feishu Bitable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moljay](https://clawhub.ai/user/moljay)

### License/Terms of Use:

MIT-0

## Use Case:

External participants use this skill to submit coffee chat signup details through an AI assistant, while organizers use it to deduplicate WeChat IDs and write registrations to Feishu Bitable through a relay service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill collects personal contact data and sends it to an externally operated relay and Feishu table.

Mitigation: Use only with a trusted relay operator and table owner, disclose the data destination to participants, and replace the default endpoint or API key before deployment.

Risk: The ping success response can present a misleading deployment-style confirmation after signup.

Mitigation: Review and revise the ping confirmation so the user-facing result truthfully describes the registration outcome.

Risk: Duplicate and overwrite handling depends on the relay behavior and can affect existing signup records.

Mitigation: Require server-side duplicate and overwrite checks before production use, and preserve explicit user confirmation for overwrites.

## Reference(s):

- [Skill README](artifact/README.md)
- [Relay Server README](artifact/relay-server/README.md)
- [Feishu Open Platform](https://open.feishu.cn)
- [ClawHub skill page](https://clawhub.ai/moljay/skills/fork-latte-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Collects name, occupation, WeChat ID, and entrepreneurship experience; may call a configured relay endpoint for duplicate checks and submissions.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
