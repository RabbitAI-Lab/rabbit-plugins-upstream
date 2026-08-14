## Description:

使用百度地图地址文本进行零售连锁拓店选址分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

Retail expansion, operations, and site-selection teams use this skill to analyze published retail store snapshots, compare brand coverage, assess candidate address competition, and organize next-step field verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand, address, and coordinate queries may be sent to the publisher's API.

Mitigation: Use the skill only in a controlled environment and avoid submitting sensitive or confidential location data.

Risk: The skill requires a DDT_API_KEY for API calls.

Mitigation: Store the API key in the local or controlled runtime environment and do not paste it into chats, logs, skill files, or version control.

Risk: Published snapshots and limited previews may be incomplete or unsuitable as the sole basis for expansion decisions.

Mitigation: Treat outputs as an initial screening aid and verify candidate sites, coverage gaps, and competitive context through field checks and authoritative business sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-retail-expansion)
- [店店通 ClawHub API homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses published retail snapshots and limited previews; avoids exposing API keys, internal identifiers, suppliers, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
