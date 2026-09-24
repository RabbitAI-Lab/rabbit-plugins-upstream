## Description:

Shorten a talking-head video with Yaps Auto Cut. Review the pauses, adjust the cut, and export. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT-0

## Use Case:

External users and video creators use this skill to shorten talking-head videos with Yaps Auto Cut, review detected pauses and cut plans, tune pacing, and export a new trimmed video while preserving the source file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke broader local Yaps actions than its video-clipping description makes obvious.

Mitigation: Review before installing, keep tasks limited to intended videos, and confirm the Yaps CLI command group and flags before processing.

Risk: The skill checks local Yaps installation and account readiness and may open Yaps during account recovery.

Mitigation: Use it only where local Yaps automation is expected, do not approve credential prompts on the skill's behalf, and sign in or manage access inside Yaps.

Risk: Video processing can expose local media content to the agent host and create or retain Yaps projects, history, and usage state.

Mitigation: Select only intended input videos, preserve sources and existing outputs with new filenames, and avoid giving unrelated sensitive media or documents to the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-video-clipping)
- [Runtime guide](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Yaps CLI commands and links to produced media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a rendered MP4 output through the local Yaps app and reports metrics such as source duration, kept duration, removed percentage, cut count, and longest retained gap.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
