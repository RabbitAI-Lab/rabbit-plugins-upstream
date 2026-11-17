## Description:

LinkedIn automation skill for searching people and companies, fetching profiles, sending messages and InMails, managing connections, creating posts, reacting, commenting, and using Sales Navigator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vprudnikoff](https://clawhub.ai/user/vprudnikoff)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to run LinkedIn account automation from an agent, including profile and company lookup, outreach messaging, connection management, content posting, reactions, comments, and Sales Navigator workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable Linked API and identification tokens may be exposed through agent chat, shell history, process listings, or logs.

Mitigation: Use an isolated environment, avoid pasting reusable tokens into chat or visible command lines, and rotate or revoke any token that may have been exposed.

Risk: The skill can perform live LinkedIn account actions, including messages, InMails, connection changes, posts, comments, reactions, workflow runs, and account resets.

Mitigation: Require explicit user review and confirmation before every account-modifying command.

Risk: The skill depends on a third-party npm package and Linked API cloud browser service.

Mitigation: Install only when the package source and Linked API service are trusted, and pin the CLI version in the execution environment.

Risk: Queued, slow, or rate-limited operations can produce delayed or partial outcomes.

Mitigation: Check the JSON success field, exit code, and workflow status before retrying or taking follow-up action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vprudnikoff/skills/linkedin-skill)
- [Linked API workflow documentation](https://linkedapi.io/docs/building-workflows/)
- [Linked API app](https://app.linkedapi.io)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI actions should use --json -q; command results are machine-readable JSON with success and error fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
