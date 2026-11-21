## Description:

Make short videos through Clipwright's MCP server: an AI actor speaking your script, or a faceless video of up to 90 seconds with narration over generated scenes. Quote first for free, then start a run and collect the MP4. Clipwright returns the file and does not publish anywhere.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seocombat](https://clawhub.ai/user/seocombat)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use Clipwright to find and analyze short-form video trends, plan original scripts, and create AI-presented or faceless videos. The skill guides account setup and requires approval of paid quotes before starting paid work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan's partial assessment flags an unpinned MCP server setup, and not all referenced paths were inspected.

Mitigation: Review the MCP server source and choose a specific reviewed release before connecting.

Risk: ClawScan flags automatic feedback submission without a clear privacy warning.

Mitigation: Review what feedback is sent and when; avoid enabling feedback submission until users understand the data involved.

## Reference(s):

- [Clipwright product site](https://clipwright.io/?ref=clawhub)
- [Clipwright documentation](https://clipwright.io/docs)
- [Clipwright API OpenAPI specification](https://api.clipwright.io/openapi.json)
- [Clipwright changelog](https://clipwright.io/changelog)
- [Clipwright MCP setup](https://clipwright.io/mcp)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [MP4 video files and natural-language scripts, plans, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos are returned to the user; the skill documentation says they are not published by Clipwright.]

## Skill Version(s):

0.73.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
