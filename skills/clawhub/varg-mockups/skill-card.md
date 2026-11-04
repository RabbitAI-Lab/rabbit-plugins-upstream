## Description:

Creates self-contained HTML boards for reviewing video storyboards, image stills, visual references, and device or app UI mockups before production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and reviewers use this skill to plan and approve storyboards, visual references, generated stills, and device or app UI mockups before committing to video production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to varg for online image generation.

Mitigation: Use only references you are authorized to share with varg.

Risk: Paid image batches consume credits.

Mitigation: Review the estimated total and approve the batch before generation.

Risk: Review notes remain in the browser until cleared.

Mitigation: Clear notes after review, especially on a shared device.

Risk: The hosted service and optional downloaded rendering templates were outside the bundled-file security review.

Mitigation: Review those services and templates before use, and avoid sending sensitive material unless approved.

## Reference(s):

- [Board patterns](artifact/references/board-patterns.md)
- [Still prompts](artifact/references/still-prompts.md)
- [Board HTML template](artifact/templates/board.html)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/varg-mockups)
- [varg MCP endpoint](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Image-generation prompts, Guidance]

**Output Format:** [Self-contained HTML review board with prompts and shot specifications; review feedback can be copied as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Boards may include numbered frames, shot specs, image variants, approval statuses, and reviewer notes.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
