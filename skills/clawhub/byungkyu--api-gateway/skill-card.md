## Description:

Calls third-party APIs through Maton's gateway using credentials for apps the user has connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the skill to read or update data in a user's connected third-party apps and to manage Maton connections and hosted automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected app access and hosted automations can change records or forward account data to configured destinations.

Mitigation: Use only the scopes and accounts needed. Confirm exact records, recipients, amounts, and destinations before changes; review handlers and remove forwarding or automation when finished.

## Reference(s):

- [Maton Docs](https://docs.maton.ai)
- [API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Code, Configuration, Guidance]

**Output Format:** [App data and concise text, with shell commands, code, or configuration for requested operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected app and requested operation.]

## Skill Version(s):

1.2.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
