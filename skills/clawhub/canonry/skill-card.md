## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and analysts use this skill to guide Canonry workflows for AI visibility evidence, measurement planning, integrations, diagnostics, and reporting. It helps agents choose read, approval, and CLI paths while preserving evidence boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canonry integrations may involve sensitive provider credentials, API keys, OAuth tokens, or local credential storage.

Mitigation: Use least-privilege provider accounts, prefer token files or secret managers over command-line secret flags, restrict API keys, and keep credentials out of chat and public reports.

Risk: Server-side traffic integrations may send visitor request data to Canonry for analysis.

Mitigation: Review what visitor request data is collected and sent before enabling traffic integrations, and align collection with the operator's privacy and retention requirements.

Risk: Disconnecting an integration may not fully remove external credentials or provider-side access.

Mitigation: After disconnecting an integration, manually revoke or remove the related credentials, tokens, API keys, and provider grants.

## Reference(s):

- [Canonry ClawHub Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline JSON, shell commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approval boundaries, diagnostics, and next-step guidance based on stored Canonry evidence.]

## Skill Version(s):

5.1.3+1f10658 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
