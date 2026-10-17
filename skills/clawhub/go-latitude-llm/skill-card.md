## Description:

Guides developers using the unofficial Go client for Latitude's operations API, including projects, traces, scores, issues, API keys, and organization management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to write and review Latitude API integrations for inspecting projects, traces, and issues or performing explicitly authorized organization operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated integrations may use Latitude organization credentials or expose sensitive trace and member data.

Mitigation: Use scoped credentials where possible; keep tokens, request headers, traces, and member data out of logs, and send credentials only to a trusted API URL.

Risk: Deletes, key revocations, member changes, and exports can change organization state or email sensitive data.

Mitigation: Confirm authorization, recipients, and scope before performing these operations; test examples against a local HTTP server rather than the live API.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [Project homepage (release metadata)](https://github.com/psyb0t/go-latitude-llm)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-latitude-llm)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for credential handling, response checks, and local request testing.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
