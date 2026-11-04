## Description:

Routes requests to third-party apps the user has connected through Maton, with guidance for API calls, SDK code, and hosted or local event automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use the skill to read or update data in a named, connected app through Maton, and to manage approved functions and event automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected apps may expose sensitive data, and write actions can change or delete it.

Mitigation: Connect only the apps and permissions needed, verify the target account, and review changes before approval. Confirm deletions and secret rotations by exact ID.

Risk: Hosted functions and event destinations can run code or continuously forward event data to a URL.

Mitigation: Use a narrowly scoped account, review the code and destination before approval, and remove forwarding destinations when they are no longer needed.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and Python or JavaScript code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by connected app and requested operation.]

## Skill Version(s):

1.2.35 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
