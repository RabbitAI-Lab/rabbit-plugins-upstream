## Description:

帮助零售连锁团队使用腾讯地图复制的地点名称和地址文本分析机会城市、候选地址竞争与拓店顺序，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External retail expansion, site selection, and market planning users use this skill to convert brand names, Tencent Map address text, coordinates, or public store IDs into retail footprint, competition, coverage, and candidate-site screening guidance. The skill is not an official Tencent Map product and relies on currently published DDT store snapshot data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use requires a DDT API key and sends selected retail analysis inputs to the DDT service.

Mitigation: Use a controlled runtime, provide the key through environment variables, and do not paste secrets into chat, logs, skills, or repositories.

Risk: Returned site-selection and nearby-store results are limited previews rather than complete market or success predictions.

Mitigation: Treat outputs as initial screening guidance, preserve coverage and data-version notes, and require local validation before business decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-retail-expansion)
- [Publisher Profile](https://clawhub.ai/user/horacetu)
- [DDT Claw Homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, limited store details when requested, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated DDT API calls and should avoid exposing API keys, internal identifiers, supplier fields, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
