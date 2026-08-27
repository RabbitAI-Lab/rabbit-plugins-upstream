## Description:

Turn a user-provided PNG or JPEG line-art illustration into a hand-drawn scribe animation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[boring-stuff-club](https://clawhub.ai/user/boring-stuff-club)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn user-provided PNG or JPEG line art, diagrams, storyboards, or product concepts into MP4 scribe animations through The Scribble Thing service. The skill also guides preview, unlock, download, and deletion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded artwork and generated files are sent to an external service and retained for the current period reported by that service.

Mitigation: Call the service information tool for current limits, retention, terms, and pricing, then obtain explicit user confirmation before creating an animation.

Risk: Private management links, animation IDs, capability tokens, and unlock codes can grant access to an animation.

Mitigation: Treat these values as sensitive and avoid placing them in ordinary chat text, logs, analytics, filenames, or unrelated tools.

Risk: Users may upload artwork they do not have rights to process.

Mitigation: Ask the user to confirm they have the necessary rights before sending the image to the service.

Risk: Generated video content may be large or unsuitable for model context.

Mitigation: Provide short-lived download URLs rather than placing video bytes into the model context.

## Reference(s):

- [The Scribble Thing MCP endpoint](https://scribble.boringstuff.club/mcp)
- [The Scribble Thing REST fallback guide](https://scribble.boringstuff.club/docs/agent-api)
- [ClawHub skill page](https://clawhub.ai/boring-stuff-club/skills/the-scribble-thing)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown text with private links to generated MP4 animation previews or downloads and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses short-lived download URLs; animation IDs, capability tokens, management links, and unlock codes are sensitive.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
