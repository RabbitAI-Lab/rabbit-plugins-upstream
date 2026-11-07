## Description:

Creates HTML review boards for video stills, hosted mockup images, and locally rendered device or app UI mockups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers and creative teams use the skill to prepare numbered stills, storyboards, moodboards, and UI mockups for review before committing to video production. Reviewers can approve or flag frames and return feedback as Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted image generation sends prompts and selected references to Varg.

Mitigation: Use only material you are authorized to upload and approve the quoted generation cost before submitting.

Risk: The hosted service, external template code, and companion skills were not audited for this release.

Mitigation: Review those external components before relying on them for sensitive work.

Risk: Review notes remain in the browser until cleared.

Mitigation: Clear saved board notes when they should no longer remain on the device.

## Reference(s):

- [Board patterns](references/board-patterns.md)
- [Still prompt guide](references/still-prompts.md)
- [Varg MCP endpoint](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [HTML, Images, Markdown, Code]

**Output Format:** [Self-contained HTML review boards, generated still images, local UI mockups, and Markdown feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Boards organize numbered frames with shot details, prompts, variants, and review notes.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
