## Description:

Supports Temu EU returns, refunds, and after-sales workflows through LinkFox gateway scripts for querying after-sales records, return logistics, return addresses, return labels, signatures, carriers, and label uploads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu EU sellers, support operators, and developers use this skill to inspect and process returns/refunds and after-sales data through the LinkFox Temu gateway. It helps agents prepare authenticated API calls, interpret JSON responses, and save response artifacts for follow-up analysis.

### Deployment Geography for Use:

Europe (Temu EU Partner site)

## Known Risks and Mitigations:

Risk: Credential handling and local token storage can expose LinkFox or Temu tokens if used in shared workspaces or logs.

Mitigation: Use the skill only in trusted workspaces, avoid plaintext local token storage unless accepted by policy, keep token-listing commands masked, and rotate any token that may have been exposed.

Risk: Broad proxy and file-download scripts can reach more Temu operations than the narrow EU returns/refunds workflow requires.

Mitigation: Restrict use to the documented EU returns/refunds endpoints, review requested API types before execution, and prefer a narrower deployment that exposes only required endpoints.

Risk: The skill saves complete API responses to a local linkfox session data directory, which may retain order, after-sales, or refund data.

Mitigation: Run in an approved workspace, review saved response files for sensitive data, and remove retained artifacts according to the user's data-handling policy.

Risk: Billing and onboarding helpers may initiate account, plan, or payment-related flows.

Mitigation: Require explicit user approval before running onboarding or billing commands and verify plan/payment details outside shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-eu)
- [API reference](artifact/references/api.md)
- [Temu accessToken authorization](artifact/references/access-token.md)
- [Partner EU returns and refunds catalog](artifact/references/partner-eu-catalog.md)
- [Returns and refunds API index](artifact/references/apis/README.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses are summarized while complete JSON is written under a linkfox session data directory.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
