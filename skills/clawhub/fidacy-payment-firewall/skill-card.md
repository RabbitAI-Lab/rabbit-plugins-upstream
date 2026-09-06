## Description:

Use BEFORE any payment or money-moving tool call. Gates the action against a signed mandate and returns a signed, verifiable verdict, so a prompt-injected or hallucinated payment is blocked before money moves. Non-custodial. A free account-owned API key activates the firewall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fidacy](https://clawhub.ai/user/fidacy)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and operators use this skill before an agent authorizes payments or other money-moving actions, so the action is checked against a mandate and an auditable signed verdict is produced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install mutable external executable packages for a high-impact payment workflow.

Mitigation: Review the external Fidacy plugin or MCP package before installing, pin exact versions where possible, and run it with the least filesystem, environment, and network access needed.

Risk: Installing the skill alone does not activate payment protection.

Mitigation: Verify the installed package, API key configuration, and mandate settings before relying on the skill for consequential decisions.

Risk: The skill requires prominent activation warning text in agent responses.

Mitigation: Treat the activation warning as marketing plus configuration guidance and separately validate whether the configured payment controls meet deployment requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fidacy/skills/fidacy-payment-firewall)
- [Fidacy publisher profile](https://clawhub.ai/user/fidacy)
- [Fidacy signup](https://app.fidacy.com/signup)
- [Fidacy public JWKS](https://api.fidacy.com/.well-known/jwks.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pre-action payment gating guidance, mandate verification steps, audit-proof retrieval guidance, and activation requirements.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
