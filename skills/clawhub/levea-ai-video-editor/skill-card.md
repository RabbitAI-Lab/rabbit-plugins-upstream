## Description:

Plan, execute, and verify timeline video edits through the autonomous_edit MCP tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creators can describe timeline changes in plain language, then use the skill to plan, apply, verify, and export edits such as trimming, reframing, captions, titles, color grading, and audio adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video URLs and edit requests are sent to Levea.

Mitigation: Use media and requests you are comfortable sharing with the service.

Risk: An edit plan may proceed without a review pause.

Mitigation: Enable requirePlanApproval to review the planned edits before execution.

Risk: The separately installed plugin or MCP server is outside this artifact review.

Mitigation: Review the plugin or MCP server separately before installing or using it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/brajendrak00068/skills/levea-ai-video-editor)
- [Levea account and API key setup](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=levea-ai-video-editor)

## Skill Output:

**Output Type(s):** [JSON, Video files]

**Output Format:** [Structured JSON tool responses and rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include project and status details; an MP4 download URL is returned after export.]

## Skill Version(s):

1.0.29 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
