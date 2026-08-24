## Description:

AI电商专家｜抖音电商 图片视频全内容 helps Douyin ecommerce merchants and operations, design, advertising, and agency teams prepare IMIVA MCP workflows for product images, detail content, and video materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce merchants, content operators, designers, media buyers, and agency teams use this skill to turn product materials, audience goals, channel requirements, and budget constraints into IMIVA MCP calls for Douyin ecommerce listing, seeding, advertising, and conversion content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs the IMIVA npm package using an unpinned @latest version and passes the local environment to that process.

Mitigation: Install only in a trusted environment, pin the npm package version before operational use, and expose only the required MCP_TOKEN and API_URL variables.

Risk: Product assets and task data may be sent to the IMIVA service during MCP use.

Mitigation: Use approved product assets, avoid secrets or unnecessary personal data in prompts and files, and confirm that IMIVA processing is acceptable for the intended business workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-douyin-ecommerce-content)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON MCP arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP task parameters, dry-run budget checks, task IDs, polling guidance, and content review criteria.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
