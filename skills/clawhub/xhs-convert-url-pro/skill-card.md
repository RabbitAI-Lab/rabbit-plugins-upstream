## Description:

小红书笔记链接批量转链工具，可把小红书笔记链接和 xhslink 短链转换为携带 xsec_token、可在浏览器打开的新链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to register or log in to a third-party Xiaohongshu URL conversion service, check quota, submit one or more note URLs, and return converted browser-openable links. The skill is intended for normal ClawHub use and includes paid quota-consuming conversion flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu URLs to a third-party conversion backend.

Mitigation: Use it only with URLs the user agrees to submit to that backend, and disclose that conversion depends on the third-party service.

Risk: The skill stores an account token in a local user configuration file.

Mitigation: Keep the configuration file private, do not commit or share it, and use logout or token rotation if the token may have been exposed.

Risk: Conversions consume paid quota after registration or login.

Mitigation: Confirm with the user before registration, login, or submitting quota-consuming batches, and check quota before bulk conversion.

Risk: The default backend uses HTTP and the CLI can disable HTTPS certificate checks when configured.

Mitigation: Avoid enabling insecure TLS settings unless the user explicitly accepts the transport risk, and prefer a trusted HTTPS endpoint when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cuiyunhai/skills/xhs-convert-url-pro)
- [Publisher profile](https://clawhub.ai/user/cuiyunhai)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and parsed JSON results from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful conversions return ordered converted URLs; CLI stdout is JSON while prompts and progress are written to stderr.]

## Skill Version(s):

1.1.0 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
