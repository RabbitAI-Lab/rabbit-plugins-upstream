## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Canonry to inspect stored AI visibility and site evidence, diagnose changes, plan measurement, and review integrations or reports before approving live actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live provider reads, writes, syncs, and external actions can consume quota or change connected services.

Mitigation: Review commands and approve only the exact target and bounded action before execution.

Risk: Configuration and token files may expose OAuth secrets or API keys.

Mitigation: Keep local credentials private with restrictive permissions; never paste secrets into chat.

Risk: Repeating a write after an ambiguous response may duplicate an action.

Mitigation: Inspect saved state or the operation receipt before retrying; stop when the outcome remains unclear.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [AEO analysis](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile integration](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline CLI commands and structured evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live reads and changes require approval for the specific target and bounded action.]

## Skill Version(s):

7.45.1+c90d226 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
