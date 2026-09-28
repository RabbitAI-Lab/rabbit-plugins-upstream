## Description:

Helps agents use Canonry's connected tools or CLI to inspect visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, site operators, and their agents use this guide to interpret Canonry's stored AI-visibility evidence, plan measurement, and prepare approved site and marketing workflows through connected tools or the optional CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI-guided writes, provider reads, syncs, schedules, and live-site changes may alter operations or incur usage costs.

Mitigation: Require explicit approval before these actions and prefer staging or dry runs for live-site work.

Risk: Google Ads operations can affect advertising spend.

Mitigation: Review the exact paid-advertising action and its spend implications before approval.

Risk: Provider keys and OAuth tokens may be exposed if shared with an agent.

Mitigation: Keep secrets out of chat and use least-privilege, project-scoped credentials.

## Reference(s):

- [Canonry ClawHub release](https://clawhub.ai/arberx/skills/canonry)
- [CLI commands and return shapes](artifact/references/canonry-cli.md)
- [Interpreting visibility results](artifact/references/aeo-analysis.md)
- [Indexing workflows](artifact/references/indexing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)
- [Server-side traffic](artifact/references/server-side-traffic.md)
- [Google Business Profile](artifact/references/google-business-profile.md)
- [Google Ads and GTM](artifact/references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve evidence scope and distinguish observed results from hypotheses; operational changes require explicit approval.]

## Skill Version(s):

5.28.0+a39f687 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
