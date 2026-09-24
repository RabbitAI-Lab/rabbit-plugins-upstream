## Description:

Make a meeting transcript with speaker labels in Yaps. Correct it, export it, or ask questions. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, and developers use this skill from a local agent session to create speaker-labeled meeting transcripts in Yaps, correct labels or text with user confirmation, export results, generate recaps, and ask grounded questions about a meeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Yaps commands against selected meeting media and local files.

Mitigation: Install only when the agent should use the local Yaps installation, select only requested inputs, and review local command use before approval.

Risk: Yaps projects, project audio, and history may persist in the local Yaps application after the agent task.

Mitigation: Expect durable local Yaps state, preserve existing exports, and inspect existing projects before retrying long or failed jobs.

Risk: Unexpected credential prompts or unrequested fallback uploads could expose account or media data.

Mitigation: Do not approve unexpected credential prompts, do not create separate plugin accounts, and do not upload source media to another service unless explicitly requested.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-meeting-transcription)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text responses, with structured JSON results from local Yaps commands summarized for the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Meeting projects and history remain in local Yaps; exports should use new output paths and preserve existing files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
