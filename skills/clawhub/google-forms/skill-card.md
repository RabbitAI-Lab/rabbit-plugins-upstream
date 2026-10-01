## Description:

Connect to Google Forms through Maton to create forms, add questions, and retrieve responses with managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams managing Google Forms can use this skill to create forms, add questions, and retrieve responses through their authorized connection. Optional hosted functions and scheduled or external-event triggers can automate actions with user approval; Google Forms itself is not a trigger source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connection could authorize broader Google Forms access than the task needs.

Mitigation: Review OAuth scopes and request only the access needed; confirm new connections and writes with the user.

Risk: Persistent triggers and destinations can keep forwarding sensitive event data to a URL.

Mitigation: Confirm the automation and destination with the user, verify who controls the URL, and review or remove unneeded forwarding.

Risk: The API-key fallback uses a long-lived credential.

Mitigation: Prefer managed OAuth; use an API key only when the CLI cannot be installed and avoid exposing it to child processes or logs.

## Reference(s):

- [Maton](https://maton.ai)
- [Google Forms API reference](https://developers.google.com/workspace/forms/api/reference/rest)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown guidance and command examples; JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions depend on the user's authorized Google Forms connection; writes and automation require confirmation.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
