## Description:

AI电商专家｜微信小店与视频号 图片视频全内容 helps WeChat Store and Video Channel merchants, operators, designers, ad teams, and agency teams prepare IMIVA MCP requests for product images, detail-page content, ecommerce videos, campaign assets, task tracking, and result review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams use this skill to turn product facts, media assets, audience, channel, format, and budget constraints into executable IMIVA MCP workflows for WeChat Store and Video Channel content. It supports setup guidance, credit checks, dry-run validation, paid task submission, task lookup, and output quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an unpinned remote npm package with the user's IMIVA token and inherited environment.

Mitigation: Review before installation, prefer pinning the npm package version, restrict the subprocess environment, and use an IMIVA token with the minimum permissions available.

Risk: Paid IMIVA generation tasks can consume credits if submitted without budget confirmation.

Mitigation: Run dry-run or credit checks first, confirm estimated credits with the user, and set maxCredits before creating paid tasks.

Risk: Local product media paths may upload files to IMIVA during generation workflows.

Mitigation: Provide only local media files intended for IMIVA upload and avoid running from a shell that exposes unrelated sensitive files or secrets.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-wechat-video-channel-ecommerce-content)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP tool names, JSON arguments, local file or HTTPS media references, credit checks, task IDs, and review guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
