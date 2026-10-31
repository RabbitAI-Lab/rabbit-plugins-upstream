## Description:

Compile and execute multi-step video editing plans with automated timeline verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use the skill to carry out multi-step timeline edits, verify the result, and export an MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video editing uses Levea's cloud service, so source media is sent to that service.

Mitigation: Use media you are comfortable sending to Levea.

Risk: Applying an edit could change a valuable project.

Mitigation: Enable requirePlanApproval to review the planned changes before applying them.

Risk: The separate OpenClaw plugin or MCP server has its own security considerations.

Mitigation: Review the plugin or MCP server separately, keep the API key in its tool configuration, and inspect exports before sharing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/brajendrak00068/skills/ai-agentic-video-editor)
- [Levea editing service](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=ai-agentic-video-editor)
- [Levea API](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [Video edits, Timeline verification, MP4 video, Structured project status and export details]

**Output Format:** [Edited project with a structured status response and, after export, an MP4 URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edits can pause for approval; rendering may complete synchronously or through a queued job.]

## Skill Version(s):

1.0.27 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
