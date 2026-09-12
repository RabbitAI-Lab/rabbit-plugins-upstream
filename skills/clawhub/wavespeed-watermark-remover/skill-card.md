## Description:

Helps agents remove watermarks, logos, captions, and text overlays from user-owned or licensed images and videos with WaveSpeed AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operations teams use this skill to route eligible image or video watermark-removal requests through WaveSpeed AI. It is intended for media the user owns or is licensed to modify, with guardrails against removing third-party copyright, attribution, or preview marks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media is uploaded to WaveSpeed's cloud service for processing.

Mitigation: Only process media the user is comfortable sending to WaveSpeed and that the user owns or is licensed to modify.

Risk: Watermark removal can be misused to strip third-party copyright, attribution, or stock preview marks.

Mitigation: Confirm ownership or license before running the model, refuse unclear or infringing requests, and avoid outputs that misrepresent authorship or licensing.

Risk: The documented setup uses global npm and npx commands that may install changing package versions.

Mitigation: Pin reviewed package versions where possible and run the CLI or MCP server in a least-privileged environment.

Risk: Authentication material may be exposed if users paste keys into chat or commands are run in shared environments.

Mitigation: Use `wavespeed login` or a scoped `WAVESPEED_API_KEY` environment variable and never ask the user to paste secrets into the conversation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-watermark-remover)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces WaveSpeed CLI or MCP invocation guidance and result URLs; media processing happens through WaveSpeed's cloud service.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
