## Description:

Helps agents find Brazilian addresses, nearby postal codes and businesses using PontoFato's address and company data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can look up Brazilian postal codes, address coordinates, building units and nearby businesses, or summarize business activity around a location.

### Deployment Geography for Use:

Brazil

## Known Risks and Mitigations:

Risk: Address and location lookups send queries to PontoFato.

Mitigation: Share only the lookup details needed for the task.

Risk: Paid API calls may spend prepaid credit or expose access tokens.

Mitigation: Confirm the price and action with the user before paid calls, and keep cred_, mmk_ and mmw_ tokens private.

## Reference(s):

- [PontoFato skill on ClawHub](https://clawhub.ai/wrpbr/skills/pontofato)
- [PontoFato API reference](https://pontofato.com/llms-full.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text, optionally with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available 2022 address data and the date of the company records.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
