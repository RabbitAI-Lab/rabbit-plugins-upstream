## Description:

Reframe horizontal 16:9 footage into 9:16 vertical short-form videos with subject tracking and captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, and developers use this skill to turn horizontal footage into vertical short-form videos, keep speakers framed, trim clips, and add captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source footage is shared with the Levea editing service.

Mitigation: Use only footage you are authorized to share with Levea.

Risk: An exposed Levea API key could allow unauthorized service access.

Mitigation: Protect the API key and store it in the plugin or MCP server configuration rather than including it in prompts.

Risk: Automated edits may not match the intended framing or captions.

Mitigation: Set requirePlanApproval to true to review planned edits before execution.

## Reference(s):

- [Levea editing service](https://livecore.ai/)
- [Levea API](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [Video files, Guidance]

**Output Format:** [MP4 video exports and concise project status or download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports are provided by the editing service when processing completes.]

## Skill Version(s):

1.0.2 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
