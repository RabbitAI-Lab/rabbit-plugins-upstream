## Description:

Helps agents find Brazilian addresses, nearby postal codes, and companies using PontoFato's address and business lookup tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching Brazilian locations use this skill to locate addresses and building units, find nearby postal codes, and explore companies registered around a place.

### Deployment Geography for Use:

Brazil

## Known Risks and Mitigations:

Risk: Lookups may disclose submitted postal codes, coordinates, or company identifiers to PontoFato.

Mitigation: Share only the lookup details needed and obtain appropriate consent before sending sensitive locations or identifiers.

Risk: Some lookups can incur a charge.

Mitigation: Check the current price and free allowance, then obtain the user's approval for the item and amount before using paid balance; never purchase on the user's behalf.

Risk: Prepaid credit or MCP tokens could expose account access if shared.

Mitigation: Keep cred_ and mmk_ tokens out of files, logs, and answers.

Risk: Historical address and business data may not reflect current conditions.

Mitigation: Identify address observations as 2022 census data and check the business data date before making time-sensitive claims.

## Reference(s):

- [PontoFato skill on ClawHub](https://clawhub.ai/wrpbr/skills/pontofato)
- [PontoFato API reference](https://pontofato.com/llms-full.txt)
- [PontoFato API routes and limits](https://pontofato.com/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with lookup results and optional inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include CEPs, coordinates, address units, census context, and company counts.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
