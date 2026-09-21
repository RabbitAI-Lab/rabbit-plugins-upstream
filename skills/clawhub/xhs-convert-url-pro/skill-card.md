## Description:

小红书笔记链接批量转链工具，可将小红书笔记链接和短链转换为带 xsec_token 的可打开链接，并可供 xhs-dpt 采集 skill 使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit public Xiaohongshu note URLs, poll conversion tasks, and return converted URLs with xsec_token parameters. It is intended for paid link conversion workflows and for preparing links that can be passed to the related xhs-dpt collection skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles reusable account tokens over insecure HTTP transport and can optionally disable TLS certificate verification.

Mitigation: Review before installing, avoid real accounts or paid quota until authenticated traffic uses HTTPS, and keep insecure TLS mode disabled unless tightly controlled.

Risk: Saved credentials are stored locally and shared with the xhs-dpt skill, so logout or token exposure can affect both skills.

Mitigation: Protect the local configuration file, do not commit or share saved tokens, and inform users that logout invalidates access for both skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cuiyunhai/skills/xhs-convert-url-pro)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI stdout is JSON; progress and interactive prompts are emitted on stderr.]

## Skill Version(s):

2.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
