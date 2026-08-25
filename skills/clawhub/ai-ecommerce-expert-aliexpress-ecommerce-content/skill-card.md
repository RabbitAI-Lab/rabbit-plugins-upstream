## Description:

AI电商专家｜AliExpress 速卖通 图片视频全内容 helps AliExpress merchants, operators, designers, advertising teams, and agencies prepare product images, detail-page content, social commerce assets, and video generation tasks through IMIVA MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, brand teams, designers, advertisers, and agencies use this skill to turn product assets, confirmed selling points, target channels, and output specifications into executable IMIVA MCP tasks for AliExpress listing, seeding, advertising, and conversion-oriented content. The workflow emphasizes budget confirmation, task tracking, and review of generated images, detail content, and video assets before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a mutable npm package through npx, so runtime behavior may change after publication.

Mitigation: Review the MCP client configuration before installation and prefer a pinned, reviewed package version for production environments.

Risk: The helper launches the MCP process with the user's environment, which may expose unrelated secrets to the subprocess.

Mitigation: Run it from a dedicated environment containing only the IMIVA token and required API variables, not a shell loaded with unrelated credentials.

Risk: Image and video generation tasks can consume credits or create duplicate paid work if retried carelessly.

Mitigation: Check credits first, use dry-run estimates and confirmed credit limits where supported, preserve task IDs, and query existing tasks before resubmitting.

Risk: Generated ecommerce content can include incorrect claims or copy protected creative elements if source material is not reviewed.

Mitigation: Use only user-confirmed product facts and authorized assets, and review generated images, text, and video against channel requirements before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-aliexpress-ecommerce-content)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON MCP arguments and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, query commands, budget checks, and result-review guidance for IMIVA ecommerce content workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
