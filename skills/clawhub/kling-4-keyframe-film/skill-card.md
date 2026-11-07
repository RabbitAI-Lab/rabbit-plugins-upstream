## Description:

Guides agents through making cinematic short films with Kling 4 by planning story beats, creating reference stills, generating video takes, and editing the best moments into a final cut.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and produce short narrative films, music videos, trailers, and sketches with Kling 4. It guides them from story beats and reference images through video generation and editing selected footage into a finished film.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal or confidential reference photos may be processed by an external generation service.

Mitigation: Use photos you have permission to process externally, and avoid confidential references unless the provider's handling is acceptable.

Risk: Repeated video generations and retries can increase costs.

Mitigation: Estimate each take before generation and set a budget that includes retries.

Risk: API credentials can be exposed when shared or included in logs.

Mitigation: Keep the VARG_API_KEY private and do not share commands or logs that reveal it.

Risk: External installers, companion skills, and the live MCP service were not included in the security review.

Mitigation: Install only this skill from a reviewed revision and assess external installers, companion skills, and the MCP service separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/kling-4-keyframe-film)
- [VARG how-to](https://varg.ai/how-to)
- [VARG MCP server](https://mcp.varg.ai/mcp)
- [Example Kling 4 film](https://www.youtube.com/watch?v=WzXKggH-0Io)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video files]

**Output Format:** [Markdown guidance with inline shell commands; generated video clips and final film in MP4 format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a 60–90 second film planned as 3–6 story beats, assembled from selected moments in generated takes.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
