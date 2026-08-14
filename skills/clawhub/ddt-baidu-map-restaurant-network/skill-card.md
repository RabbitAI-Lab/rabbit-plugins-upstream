## Description:

使用百度地图地址文本进行餐饮开关店与竞对分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External restaurant operations, sales, and site-selection users use this skill to analyze restaurant brand openings, closures, regional expansion, competitor density, and candidate location opportunities from published 店店通 snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brand and address queries may be sent to the 店店通 analytics API.

Mitigation: Use the skill only when that service is intended for the workflow and avoid submitting sensitive or unnecessary location details.

Risk: The DDT_API_KEY could expose access if pasted into prompts, logs, or shared outputs.

Mitigation: Store the key in a local environment variable and never display it in responses or artifacts.

Risk: Full-store-list extraction, non-restaurant requests, or unsupported metrics could lead to misleading or excessive outputs.

Mitigation: Keep analysis within published restaurant snapshots, use aggregate endpoints first, and decline unsupported sectors, full exports, and claims about revenue, profit, AUV, or closure causes.

## Reference(s):

- [店店通 DDT Claw homepage](https://gotoshop-ai.com/ddtclaw/)
- [店店通 DDT Claw API key setup](https://gotoshop-ai.com/ddtclaw/open)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-restaurant-network)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise analysis, key metrics, coverage notes, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should avoid API keys, internal identifiers, full-store-list extraction, and unsupported business conclusions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
