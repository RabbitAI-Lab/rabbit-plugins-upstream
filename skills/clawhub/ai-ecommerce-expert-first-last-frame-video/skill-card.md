## Description:

AI电商专家｜首尾帧商品视频 helps ecommerce, advertising, brand content, and social commerce teams prepare IMIVA MCP requests for first-and-last-frame product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand content teams, agencies, and developers use this skill to turn product material, channel goals, and budget constraints into IMIVA MCP calls for Seedance first-and-last-frame product video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an unpinned external npm MCP helper with broad environment inheritance.

Mitigation: Run it in a controlled shell with only the required MCP_TOKEN and API URL, and review or pin the MCP helper before enterprise deployment.

Risk: The workflow can submit paid IMIVA video generation tasks after confirmation.

Mitigation: Use dryRun to check estimated credits, require explicit budget confirmation, set maxCredits, use a unique idempotencyKey, and retain taskId for polling instead of resubmitting.

## Reference(s):

- [AI电商专家 Homepage](https://imiva.ecpro.com/)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-first-last-frame-video)
- [MCP Configuration Example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces IMIVA MCP setup guidance, video task arguments, dry-run budget checks, task polling instructions, and review criteria; it does not itself return generated media.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
