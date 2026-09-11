## Description:

Search Reddit for posts and discussions matching the user's query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to open Reddit search results in Brave for posts and discussions matching a supplied query while avoiding account changes or credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an already signed-in Brave session to view Reddit search results.

Mitigation: Use it only when Reddit should be opened in the browser; do not enter credentials and stop at the login page if authentication is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/search-reddit)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text browser navigation status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May open or reuse a Brave browser tab and should stop at Reddit login instead of entering credentials.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
