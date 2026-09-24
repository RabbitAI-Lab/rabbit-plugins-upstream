## Description:

Read MyAtriumHealth patient portal data from a shell by using the fpx CLI to relay requests through the user's signed-in Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve their own MyAtriumHealth data, including test results, medications, allergies, immunizations, health issues, visits, goals, and messages, for scripting or one-shot shell workflows. It is intended for use only with the signed-in user's own patient portal account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give shell commands broad, persistent access to live MyChart health data through a signed-in browser session.

Mitigation: Install it only when shell-level access to the user's own MyAtriumHealth data is intended, run it on a private machine, and revoke the fpx or extension pairing when persistent access is no longer needed.

Risk: Raw command output may expose personal health information in terminals, shell history, logs, or saved files.

Mitigation: Avoid saving raw outputs or tokens, project responses with jq to the minimum needed fields, and handle terminal output as sensitive health data.

Risk: Commands rely on the user's active browser session and may produce misleading empty results when the session is expired or the bridge is unavailable.

Mitigation: Run the provided session checks before data access and review command behavior before relying on returned results.

## Reference(s):

- [MyAtriumHealth endpoints - verified recipes](artifact/references/endpoints.md)
- [MyAtriumHealth helper script](artifact/references/mah.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and a Bash helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated commands and helper functions can return live patient portal data and should be reviewed before execution.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
