## Description:

Verify any Brazilian company (CNPJ) with official data: registry status, partners, sanctions, bank licence, contracts, funds. Pay per call via x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to verify Brazilian companies by CNPJ for onboarding, due diligence, sanctions screening, bank licence checks, government contract review, and investment fund checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers or search terms are sent to api.brazilayer.com for lookup.

Mitigation: Confirm the user is comfortable sending the specific CNPJ or company search term to the third-party API before making a request.

Risk: Paid routes can spend small USDC amounts through x402 or agentcash.

Mitigation: Ask the agent to confirm the exact route and listed price before any paid lookup.

Risk: Paid routes ask for payment before validating whether a CNPJ is malformed.

Mitigation: Run the free check-digit validation endpoint before using a paid route.

## Reference(s):

- [Brazilayer API Documentation](https://api.brazilayer.com/docs)
- [Brazilayer x402 Route Catalog](https://api.brazilayer.com/.well-known/x402)
- [Brazilayer Agent Economy Report](https://agenteconomy.report/s/api.brazilayer.com)
- [ClawHub Skill Page](https://clawhub.ai/aladaf/skills/brazil-kyb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Text]

**Output Format:** [Markdown with inline HTTP endpoints and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated Portuguese legal fields, registry dates, sanctions status, route recommendations, and paid lookup prices.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
