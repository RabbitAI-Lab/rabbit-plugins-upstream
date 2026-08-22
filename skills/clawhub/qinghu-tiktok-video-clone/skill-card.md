## Description:

Uses Qinghu TikTok ranking, search, video detail, product-video, and comments data to find proven video samples and turn them into reusable script templates and shooting guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to research TikTok videos through Qinghu data, identify high-performing samples, and produce reusable video script templates with storyboard, voiceover, scene, prop, and comment-insight guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API calls require a Qinghu API token and may consume paid Qinghu credits.

Mitigation: Ask for user approval before Qinghu data calls, use only a user-provided token or QINGHU_TOKEN/QHKIT_TOKEN, and report consumption from the returned pointCost value.

Risk: The skill may create local spreadsheet exports for larger result sets.

Mitigation: Tell the user when an export file is created and keep shared previews concise instead of exposing unnecessary raw data.

Risk: Generic copywriting requests could unintentionally use Qinghu data or credits.

Mitigation: Invoke this skill only for Qinghu-backed TikTok research and use a non-Qinghu workflow for generic copywriting.

Risk: Video replication guidance can be misused to copy another creator's protected materials.

Mitigation: Use source videos to learn structure, then produce original footage, wording, and assets rather than reusing the original video material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-clone)
- [Publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permission check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown responses with structured analysis, reusable script templates, concise data previews, and exported spreadsheet files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Qinghu API token; requests user approval before Qinghu data calls; reports Qinghu point consumption when paid calls are made.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
