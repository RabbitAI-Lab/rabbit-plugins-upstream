## Description:

Collect Facebook events from an event-list URL, event-search URL, or event URL through Dataify Builder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder jobs for Facebook event lists, event searches, or individual event URLs, then monitor the task and return the collected JSON result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Facebook event URLs and collection parameters to Dataify using DATAIFY_API_TOKEN.

Mitigation: Configure DATAIFY_API_TOKEN through an environment variable or managed secret store, avoid sharing the token in chat, and review collection scope before execution.

Risk: The skill can launch external collection jobs without clear per-run confirmation, which may consume account credits.

Mitigation: Confirm high-volume, multi-page, or multi-input collection scope before running and use no-wait or resume behavior rather than resubmitting paid tasks.

## Reference(s):

- [Modes and Parameters](references/modes-and-parameters.md)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-facebook-events)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task submission metadata, task status, a resume command after timeout, or the final collected JSON result.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
