## Description:

AI电商专家｜电商图片视频全套生成 helps ecommerce operations, designers, and brand marketing teams prepare IMIVA MCP tasks for coordinated product images, detail-page assets, and ecommerce videos from supplied product materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, designers, brand marketers, and operators use this skill to turn product media, selling points, channel requirements, and budget constraints into executable IMIVA ecommerce image and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an unpinned external npm package for IMIVA MCP access.

Mitigation: Review the package before use and prefer pinning a vetted package version in deployment configuration.

Risk: The helper process inherits the local environment while using MCP_TOKEN and API_URL.

Mitigation: Run with a minimal environment that contains only required variables such as PATH, MCP_TOKEN, and API_URL, and avoid shells containing unrelated account, cloud, CI, or production secrets.

Risk: Selected product media and task data are sent to the IMIVA service.

Mitigation: Use the skill only when the user trusts IMIVA for the selected materials and has rights to submit product, brand, and reference assets.

## Reference(s):

- [IMIVA AI电商专家 homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-image-video-suite)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP task arguments, budget checks, task IDs, and result-review guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
