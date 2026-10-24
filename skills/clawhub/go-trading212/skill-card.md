## Description:

Guides Go developers using an unofficial Trading 212 API client to read account data and implement explicitly requested trading actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add an unofficial Go client to projects that read Trading 212 account information or perform specifically requested order and pie operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing Trading 212 API credentials in code or logs can compromise an account.

Mitigation: Read credentials from environment variables; never commit or log them or print authorization headers.

Risk: Live orders, cancellations, and pie changes can affect real funds.

Mitigation: Use demo keys for testing and require explicit preview and confirmation of each live account action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-trading212)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-trading212)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and examples; account data and trading actions require user-run code.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
