## Description:

Generate and edit images, video, and music with Google Gemini models via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and operate a Gemini MCP server for generating or editing images, producing short videos, and creating music or audio clips from prompts and supported reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded files, URLs, clipboard images, and generated outputs may be shared with an external Google service.

Mitigation: Use only approved input data, avoid sensitive material unless policy permits it, and review generated media before reuse.

Risk: Media generation and upload workflows can incur billing or quota usage.

Mitigation: Confirm account billing status, monitor usage, and consider async/idempotency controls for long-running or repeated generations.

Risk: Installing the MCP server through npm without a fixed version can change behavior over time.

Mitigation: Pin the npm package version when deploying the skill in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gemini-mcp)
- [npm package @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets; generated media may be returned inline or as file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports image, video, music, file upload, async job, and iterative interaction workflows through Gemini MCP tools.]

## Skill Version(s):

1.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
