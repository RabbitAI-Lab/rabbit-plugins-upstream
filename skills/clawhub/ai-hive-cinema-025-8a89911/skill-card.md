## Description:

This skill guides agents through an AI-HIVE workflow for creating original low-angle sci-fi image and video concepts with cool blue lighting and orange firelight, including planning, model routing, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, directors, photographers, advertising teams, brand visual teams, and content creators use this skill to turn a visual brief into an original AI-HIVE production plan, model-routing decision, sample-generation path, task record, and acceptance checklist. It is aimed at image and video work that needs rights tracking, cost confirmation, and review before paid generation or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, task arguments, and possibly media metadata may be sent to AI-HIVE during use.

Mitigation: Install only when that service connection is acceptable, and provide only material the user is authorized to process.

Risk: The helper can send AI-HIVE credentials to an environment-selected MCP endpoint.

Mitigation: Use the default or otherwise trusted AI-HIVE MCP URL, prefer OAuth or scoped API keys, and revoke keys immediately if exposed.

Risk: Image or video generation, upload, batch, send, or publication actions may create cost or distribution risk.

Mitigation: Require explicit confirmation for model choice, budget, paid generation, uploads, batch actions, sends, and public release.

Risk: Creative outputs may raise copyright, publicity, brand, music, font, image, video, or style-imitation concerns.

Mitigation: Track material rights, use original characters and brands unless rights are proven, and review copyright risk before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-cinema-025-8a89911)
- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP Endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP Binding Guide](references/mcp-binding.md)
- [Original Workflow Card](references/original-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid generation, uploads, batch sends, or publication.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
