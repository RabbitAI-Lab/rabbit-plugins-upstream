## Description:

AI电商专家｜食品饮料电商图片视频 helps food and beverage ecommerce teams prepare IMIVA MCP workflows for product images, product detail pages, seeding creatives, marketplace listings, social commerce assets, and product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce brands, merchants, operators, designers, media buyers, and content teams use this skill to turn product materials, channel goals, audience details, and output specifications into executable IMIVA ecommerce image and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that the skill runs an unpinned external npm package.

Mitigation: Pin or independently review the npm package version before relying on the skill for production work.

Risk: The security evidence reports that the MCP process receives the full local environment.

Mitigation: Run the skill in a dedicated environment containing only the IMIVA token and required API URL, and avoid exposing unrelated account or cloud secrets.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-food-beverage-ecommerce-content)
- [MCP config example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP task parameters, task IDs, budget checks, and result-review guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
