## Description:

Guides agents using Canonry tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to navigate Canonry projects, interpret stored AI visibility evidence, plan bounded checks and changes, and prepare reports without treating proposals as approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, OAuth secrets, or other credentials could be exposed during integration setup or troubleshooting.

Mitigation: Keep secrets out of chat and reports; use the operator's secure setup flow and scoped keys where possible, then revoke unused credentials.

Risk: Live reads, research, probes, and syncs may consume quota or change saved evidence.

Mitigation: Start with stored evidence and obtain approval for the exact target and bounded operation before any live action.

Risk: WordPress edits, ad changes, Cloudflare routes, or schedules can alter externally visible behavior.

Mitigation: Review the exact change and scope before execution; stop on ambiguous outcomes and inspect saved state before retrying.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](artifact/references/canonry-cli.md)
- [Interpreting Canonry results](artifact/references/aeo-analysis.md)
- [Indexing workflows](artifact/references/indexing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)
- [Server-side traffic](artifact/references/server-side-traffic.md)
- [Google Business Profile integration](artifact/references/google-business-profile.md)
- [Google Ads and Tag Manager](artifact/references/google-marketing.md)
- [Google Marketing setup guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples and evidence-based summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes stored evidence from hypotheses and flags missing or stale measurements.]

## Skill Version(s):

5.20.0+b536605 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
