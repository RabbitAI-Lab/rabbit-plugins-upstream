## Description:

AI电商专家｜美妆护肤电商图片视频 helps beauty and skincare ecommerce teams prepare IMIVA MCP requests for product images, detail pages, KOC seeding content, videos, task tracking, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External beauty and skincare brands, ecommerce merchants, operators, designers, advertising teams, and content teams use this skill to turn product assets, verified selling points, channel goals, and budget constraints into executable IMIVA ecommerce content tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an IMIVA MCP token and a mutable external npm package that can access the runtime environment.

Mitigation: Install only if the IMIVA package is trusted, use a limited token, keep the token out of chats and repositories, review available tools with list-tools, and run it away from unrelated secrets.

Risk: Creating image or video tasks may consume paid credits or duplicate work if failed tasks are resubmitted blindly.

Mitigation: Check credits, use dryRun or maxCredits where supported, confirm budget before creation, retain task IDs, and query existing tasks before submitting replacements.

Risk: Generated ecommerce assets can contain inaccurate product facts, exaggerated claims, or unauthorized use of third-party materials.

Mitigation: Use only user-provided or confirmed product facts, review generated text and visuals before publishing, and avoid copying trademarks, protected characters, people, packaging, or creative expression without permission.

## Reference(s):

- [IMIVA AI电商专家 homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-beauty-skincare-ecommerce-content)
- [IMIVA MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with JSON arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create paid IMIVA content tasks, query account and task data, and return task identifiers or generated content results through MCP.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
