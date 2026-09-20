## Description:

PanSou 网盘搜索 helps an agent search a user-configured PanSou service for cloud-drive resources across supported drive types, plugins, Telegram channels, and keyword filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[212-mei](https://clawhub.ai/user/212-mei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search a configured PanSou instance for movies, series, software, learning materials, and other cloud-drive resources. It is useful when the agent needs to filter results by drive type, plugin, Telegram channel, source, include terms, exclude terms, refresh behavior, or result format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and tokens may be sent to an untrusted or plaintext PanSou endpoint.

Mitigation: Configure only a PanSou service you control and trust, prefer an HTTPS PANSOU_URL, and avoid sending PANSOU_USER or PANSOU_PWD to third-party or plaintext endpoints.

Risk: Cached authentication tokens may be exposed if the local token file is readable by other users or processes.

Mitigation: Restrict permissions on ~/.config/pansou/token.json when authenticated mode is used and rotate credentials if the file is exposed.

Risk: Sensitive search terms may appear in URLs, browser history, proxy logs, or service logs when GET mode is used.

Mitigation: Use the default POST search mode for sensitive searches and avoid the --get option unless query exposure is acceptable.

## Reference(s):

- [PanSou skill page](https://clawhub.ai/212-mei/skills/pansou)
- [Publisher profile](https://clawhub.ai/user/212-mei)
- [PanSou GitHub deployment reference](https://github.com/fish2018/pansou)
- [API parameters](references/api-params.md)
- [Supported cloud drive types](references/cloud-types.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown guidance with shell commands and JSON search-result output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results can include clickable cloud-drive URLs and can be filtered by drive type, plugin, Telegram channel, source, include/exclude terms, refresh behavior, and response format.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
