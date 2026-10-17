## Description:

Guides Go developers using the unofficial PostGrid client to manage print and mail resources and verify addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations for PostGrid print and mail services and address verification, including authenticated requests and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed PostGrid API credentials can enable unauthorized requests.

Mitigation: Read POSTGRID_API_KEY from the environment; never commit or log the key.

Risk: Live mail actions and bulk verification or targeted list operations can affect real resources or incur charges.

Mitigation: Develop with a test key and review generated code before running live create, send, cancel, delete, bulk verification, or targeted list operations.

Risk: Retrying mail creation after an uncertain response can submit a duplicate request.

Mitigation: Check whether the first request succeeded before retrying.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go client project (skill homepage; not verified release provenance)](https://github.com/psyb0t/go-postgrid)
- [PostGrid API specification source](https://raw.githubusercontent.com/postgrid/postgrid-node/main/.stats.yml)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for authenticated PostGrid requests, response handling, and local testing.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
