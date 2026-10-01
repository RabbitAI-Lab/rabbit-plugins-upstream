## Description:

Helps remove text and watermarks from selected images and videos, erase video subtitles, and resolve supported share links to watermark-free video URLs through 550W AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinehu](https://clawhub.ai/user/sunshinehu)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other authorized users can clean up selected images and videos or resolve supported video share links. Processing uses 550W AI and may consume account credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media or public links are sent to 550W AI for processing and may consume account credits.

Mitigation: Use only authorized media; explain transmission and possible charges, and obtain approval before each paid upload or submission.

Risk: API keys on a shared or untrusted machine may expose account access.

Mitigation: Prefer OAuth when supported; store API keys only on a trusted single-user machine and never include them in logs or commands.

Risk: Deleting a task may remove the associated media without refunding credits.

Mitigation: Confirm the exact task with the user immediately before deletion.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinehu/skills/550w-ai-mcp-subtitle-watermark-removal)
- [550W OAuth connection](https://eraser.550wai.com/mcp-connect/)
- [550W API access](https://eraser.550wai.com/api/)

## Skill Output:

**Output Type(s):** [Text, Guidance, URLs]

**Output Format:** [Markdown text with task status and media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task identifiers or a resolved video URL; resolving a link does not guarantee a local download.]

## Skill Version(s):

3.1.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
