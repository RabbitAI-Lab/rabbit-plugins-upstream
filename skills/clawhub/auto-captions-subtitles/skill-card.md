## Description:

Generate synchronized word-by-word animated captions and translated subtitles for video timelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT

## Use Case:

Video editors and creators use this skill to generate word-timed animated captions, style subtitles, and translate captions on a video timeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted videos may contain content the user does not want to share with the editing service.

Mitigation: Submit only videos the user is comfortable sharing with Levea.

Risk: The Levea API key stored in plugin or MCP configuration could be exposed.

Mitigation: Protect the API key and restrict access to the tool configuration where it is stored.

Risk: An automatically proposed timeline edit may not match the user's intent.

Mitigation: Enable requirePlanApproval and review the proposed edit before it runs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/brajendrak00068/skills/auto-captions-subtitles)
- [Create a Levea account and API key](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=auto-captions-subtitles)
- [Levea API endpoint](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [API Calls, Text, Video files, URLs]

**Output Format:** [Tool response with project status and identifiers, plus an MP4 export URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports may complete asynchronously; a project ID supports follow-up edits.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
