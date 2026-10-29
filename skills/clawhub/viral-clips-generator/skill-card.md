## Description:

Identify high-engagement moments in long-form recordings and extract standalone short-form video clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and video editors use this skill to identify engaging moments in long recordings and export them as short-form clips, optionally with vertical reframing and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source footage is sent to Levea for cloud processing.

Mitigation: Use only footage you are comfortable having Levea process.

Risk: The editing integration requires a Levea API key.

Mitigation: Protect the API key in the plugin or MCP server configuration.

Risk: Edits can be run without an explicit plan review when approval is not enabled.

Mitigation: Set requirePlanApproval to true when you want to approve the edit plan first.

## Reference(s):

- [Highlight Clip Extractor on ClawHub](https://clawhub.ai/brajendrak00068/skills/viral-clips-generator)
- [Levea account and API key setup](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=viral-clips-generator)

## Skill Output:

**Output Type(s):** [Video clips, Project status and export links]

**Output Format:** [MP4 video and tool response fields such as project ID, status, and export URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multiple standalone clips, vertical reframing, captions, and a consolidated archive.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
