## Description:

Guides developers in using an unofficial typed Go client to read and write HubSpot API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add a typed Go HubSpot client and implement authenticated API calls for CRM records and other HubSpot data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot access tokens or developer keys could be exposed in code, logs, or source control.

Mitigation: Use least-privilege credentials from environment variables and keep credentials and request headers out of logs and commits.

Risk: Generated code could change, delete, or purge live CRM records.

Mitigation: Review write and delete operations before running them against a live account and limit changes to records the task owns.

## Reference(s):

- [go-hubspot project homepage](https://github.com/psyb0t/go-hubspot)
- [Setup and reference](references/setup.md)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides typed request and response examples; does not itself execute HubSpot operations.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
