## Description:

Plans, applies, verifies, and exports video edits from natural-language requests through the Levea editing service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to turn natural-language requests into planned edits, captions, short clips, and video exports in Levea.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video project context, prompts, media references, and job data are sent to the Levea API.

Mitigation: Use the skill only when sharing that content with Levea is acceptable.

Risk: Automated edits can alter or remove content unexpectedly.

Mitigation: Review the planned edits and require explicit approval before important or destructive changes.

Risk: Exports and queued generation jobs may incur costs or take time.

Mitigation: Confirm export costs and review queued jobs before proceeding.

Risk: The optional README setup can install an unpinned MCP server version.

Mitigation: Pin the MCP server version when using that setup path.

## Reference(s):

- [AI Agentic Video Editor on ClawHub](https://clawhub.ai/brajendrak00068/skills/ai-agentic-video-editor)

## Skill Output:

**Output Type(s):** [Text, JSON, Video export links]

**Output Format:** [JSON edit summaries and scene results, with export links or job IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports may be delivered asynchronously as MP4 videos or ZIP bundles; poll job status for pending results.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
