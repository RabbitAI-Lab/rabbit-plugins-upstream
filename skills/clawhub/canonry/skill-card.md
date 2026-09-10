## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, developers, and analysts use this skill to navigate Canonry evidence, diagnose AI visibility changes, plan measurement, review integrations, and prepare reports through MCP tools or the `cnry` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting real provider accounts can expose credentials or project-scoped keys if operators paste secrets into chat, shell history, or recorded terminals.

Mitigation: Use least-privileged provider accounts and project-scoped keys, keep tokens in secure stores or mode-0600 files, avoid passing secrets through agent transcripts, and rotate any exposed keys.

Risk: Server-side traffic workflows can process raw visitor URLs, referrers, and IP addresses for classification.

Mitigation: Confirm the data flow meets privacy and compliance requirements before enabling traffic collection, and rely on the documented bounded samples and aggregation behavior when reviewing reports.

## Reference(s):

- [Canonry Operations Guide v1](SKILL.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic (AI Visibility - Server-Side)](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and references to structured JSON outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to inspect MCP tool schemas and server-returned metrics before acting.]

## Skill Version(s):

4.191.0+2bcbc86 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
