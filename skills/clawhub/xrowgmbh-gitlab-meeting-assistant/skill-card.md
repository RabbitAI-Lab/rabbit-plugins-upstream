## Description:

Capture features and bugs as sanitized GitLab issues during planning meetings, only on the requester's explicit instruction. Use for GitLab Meeting Assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Teams use the skill during planning meetings to turn discussed feature requests and bugs into sanitized GitLab issues. The requester selects the project and explicitly asks before any issue is created.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential meeting details or secrets could be disclosed if sanitization is incomplete.

Mitigation: Sanitize and inspect all issue fields and attachments before each write; create issues as confidential from the outset.

Risk: An issue could be sent to the wrong GitLab project if the destination is inferred or carried over ambiguously.

Mitigation: Use the project explicitly selected for the current meeting and ask when it is missing or ambiguous.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-meeting-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [English GitLab issue titles and descriptions, with Markdown where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Issue content is sanitized and created confidentially only after an explicit request.]

## Skill Version(s):

1.124.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
