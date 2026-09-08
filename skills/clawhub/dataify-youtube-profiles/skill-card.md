## Description:

Collect YouTube channel or profile records by channel URL or keyword. Do not use for videos, comments, transcripts, or media downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs that collect YouTube channel/profile records by channel URL or keyword, monitor the asynchronous task, and return collected JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API token exposure

Mitigation: Configure DATAIFY_API_TOKEN in the environment and avoid pasting tokens into chat or generated output.

Risk: Data and credit use through Dataify

Mitigation: Use only when the user intends to submit YouTube channel URLs or keywords to Dataify, and confirm higher-volume or multi-page collection scopes before execution.

Risk: Out-of-scope YouTube collection

Mitigation: Keep usage limited to YouTube profile/channel collection and do not use it for videos, comments, transcripts, or media downloads.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-youtube-profiles)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a Dataify API token from DATAIFY_API_TOKEN and may return a task ID, status, parameters, file name, message, and final collected results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
