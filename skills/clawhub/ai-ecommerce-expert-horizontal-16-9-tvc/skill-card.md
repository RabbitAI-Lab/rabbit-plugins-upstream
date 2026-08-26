## Description:

AI电商专家｜16:9 电商 TVC 广告 helps ecommerce, brand, advertising, and video teams prepare and submit IMIVA MCP requests for commercial 16:9 product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand content teams, advertisers, video editors, and social commerce teams use this skill to turn product materials, audience details, channel requirements, budget checks, and output specifications into IMIVA video-generation tasks for 16:9 TVC-style ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an npm-based MCP service with access to an MCP token and selected product media.

Mitigation: Use it only with a trusted IMIVA account and package source, pin the npm package version where possible, and pass only the required MCP_TOKEN and API_URL or IMIVA_API_URL environment variables.

Risk: Video-generation tasks can consume paid credits if submitted without review.

Mitigation: Run dryRun checks first, review estimatedCredits, set maxCredits to the approved limit, and use an idempotency key for each paid task.

Risk: Product claims, protected brand elements, or third-party reference media could be used incorrectly in generated ecommerce ads.

Mitigation: Use only authorized source media and user-confirmed product facts, then review the generated video for accurate claims, branding, text, and channel fit before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-horizontal-16-9-tvc)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces IMIVA MCP task parameters and task-query guidance; generated media is produced by the external IMIVA service.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
