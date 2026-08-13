## Description:

Helps agents work with Temu Europe returns, refunds, and after-sales workflows through LinkFox-proxied Partner EU APIs for after-sales order lookup, return logistics, return addresses, return labels, carriers, signatures, uploads, and signed file download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu EU sellers, operators, and developers use this skill to query and manage returns, refunds, and related after-sales records through LinkFox gateway scripts and reference documentation.

### Deployment Geography for Use:

Europe (Temu Partner EU)

## Known Risks and Mitigations:

Risk: The skill can act as a broader LinkFox/Temu gateway than its returns and refunds title may imply.

Mitigation: Review the scripts and invoked API type before use, and limit use to the Temu EU returns, refunds, and after-sales operations needed for the task.

Risk: Credential handling includes LinkFox API keys, Temu access tokens, and optional local token storage.

Mitigation: Use dedicated least-privilege tokens where possible, avoid shared-machine plaintext token storage, and rotate or remove saved tokens when no longer needed.

Risk: API responses and payment QR artifacts may be written to local linkfox session directories.

Mitigation: Review saved response archives for sensitive order or customer data and clean local session files after completing the workflow.

Risk: Onboarding scripts include phone login and payment-related commands.

Mitigation: Run login, plan, order, or payment commands only when explicitly registering, retrieving an API key, or purchasing credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-eu)
- [API reference](references/api.md)
- [Partner EU catalog](references/partner-eu-catalog.md)
- [API documentation index](references/apis/README.md)
- [Access token guide](references/access-token.md)
- [Authorization flow](references/authorization-flow.md)
- [Onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, JSON API responses, and local response files with summarized stdout for large payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox and Temu credentials for live API calls; scripts may save full responses under a local linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
