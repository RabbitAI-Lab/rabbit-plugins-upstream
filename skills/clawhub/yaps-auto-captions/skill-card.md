## Description:

Add captions to a video with Yaps, review words and timing, choose a style, and export the captioned video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to create, review, correct, style, render, and verify captions for video files through a local Yaps desktop installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled runtime can run broader Yaps commands and create meeting projects beyond the advertised captions workflow.

Mitigation: Install and use the skill only if you trust the publisher, and keep agent activity limited to the specific Yaps caption task and local outputs you requested.

Risk: The skill relies on a reachable local Yaps desktop installation and the user's signed-in Yaps account.

Mitigation: Confirm Yaps is installed, signed in, and authorized locally before use; do not provide API keys or approve credential prompts outside the Yaps app workflow.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-auto-captions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown responses with inline shell commands, artifact links, and concise status notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local Yaps projects and exported captioned video files when Yaps is installed and reachable.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
