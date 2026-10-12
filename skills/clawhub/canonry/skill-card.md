## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Canonry to review stored AI visibility and site evidence, diagnose changes, plan measurement, assess integrations, and prepare reports through connected tools or the optional CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live provider calls and changes to ads, WordPress, deployment, schedules, or feedback can have external effects.

Mitigation: Confirm the exact target and bounded action with the operator before proceeding; review approvals for each live operation.

Risk: Sharing API keys or OAuth credentials in chat may expose sensitive access.

Mitigation: Keep credentials in the operator's secure setup flow, not chat or reports.

## Reference(s):

- [Canonry skill on ClawHub](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](references/canonry-cli.md)
- [Interpreting Canonry results](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile integration](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe evidence scope, freshness, and uncertainty.]

## Skill Version(s):

7.44.0+89a7b4b (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
