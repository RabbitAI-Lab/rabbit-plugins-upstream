## Description:

Summarizes user-provided YouTube videos, web pages, articles, pasted text, or files already in Shorty after the user approves a Shorty summary job.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

People use this skill to get readable summaries of sources they provide, including videos, links, pasted text, and files already in Shorty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Summary jobs consume Shorty plan quota and may fetch a supplied URL from the open internet.

Mitigation: Confirm the exact source and quota use with the user before starting a job; process only sources the user intended.

Risk: Starting summary jobs requires the relevant Shorty OAuth scope.

Mitigation: If the scope is unavailable, ask the user to reconnect Shorty and approve the required scope rather than retrying the job.

## Reference(s):

- [Shorty: Summarizing Sources on ClawHub](https://clawhub.ai/bsalaeddin/skills/shorty-summarizing-sources)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary with a title and short headed sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Jobs may be queued; completed summaries are returned after status checks.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
