## Description:

Generate and edit images, video, and music with Google Gemini models through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an agent to a Gemini MCP server for image generation, image editing, short video generation, music generation, and iterative media refinement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media prompts and reference media may be sent to Gemini or the hosted connector.

Mitigation: Avoid submitting sensitive media unless the target Gemini and connector deployment are approved for that data.

Risk: Generated media may be saved in the current directory when no output directory is set.

Mitigation: Set explicit output_dir or GEMINI_OUTPUT_DIR values for sensitive work and review saved files before sharing.

Risk: Gemini API use can incur Google billing and uploaded Gemini files may persist temporarily.

Mitigation: Use billing-aware workflows, reuse idempotency keys where appropriate, and delete temporary Gemini file uploads when they are no longer needed.

## Reference(s):

- [npm package: @chrischall/gemini-mcp](https://www.npmjs.com/package/@chrischall/gemini-mcp)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)

## Skill Output:

**Output Type(s):** [Files, API Calls, Configuration instructions, Guidance]

**Output Format:** [MCP tool results with generated media file paths, optional inline media metadata, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images, video, and audio may be written to disk; some tools can also return inline results or asynchronous job identifiers.]

## Skill Version(s):

1.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
