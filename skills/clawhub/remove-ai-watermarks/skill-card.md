## Description:

Helps identify and remove AI watermark and provenance signals from images and videos the user owns or is allowed to modify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

People working with their own images and videos can inspect AI provenance signals and, where permitted, remove targeted AI labels, watermarks, or embedded metadata. The skill excludes watermarks protecting third-party paid assets.

### Deployment Geography for Use:

Global, subject to local restrictions on removing AI-generated-content labels, including in mainland China.

## Known Risks and Mitigations:

Risk: Installing dependencies and running local media-processing commands changes the user's environment or files.

Mitigation: Obtain approval for setup and file writes; use a separate output path unless overwriting is explicitly requested.

Risk: Removing provenance marks from media without rights or presenting edited media as human-made can mislead or violate applicable rules.

Mitigation: Work only on media the user owns or may modify, avoid protected third-party marks, and never treat local removal as proof of human origin.

## Reference(s):

- [Project website (release metadata)](https://raiw.cc)
- [Project repository (release metadata; import provenance unavailable)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command recipes](references/commands.md)
- [Installation and optional dependencies](references/install.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with inline shell commands and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report identified signals, caveats, and confirmed output paths; removal commands can write modified media files.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
