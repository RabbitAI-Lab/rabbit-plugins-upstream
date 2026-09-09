## Description:

Canonry helps agents operate the cnry/canonry CLI for Answer Engine Optimization, including visibility sweeps, technical audits, indexing workflows, traffic integrations, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and AEO operators use this skill to configure Canonry projects, connect search, analytics, and traffic sources, run approved sweeps and audits, and interpret mention and citation results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Canonry runtime can handle locally stored service credentials and API keys.

Mitigation: Use least-privilege, project-scoped, or read-only keys where possible; protect ~/.canonry/config.yaml with restrictive permissions; and do not paste secrets into chat or shell history.

Risk: Server-side traffic and Cloudflare Worker paths can send raw visitor metadata off the site.

Mitigation: Review the Worker route and traffic path before enabling them, and confirm the data handling posture with the site owner.

Risk: Some Canonry actions can mutate projects, publish changes, or consume provider quota.

Mitigation: Require explicit operator approval for mutations, quota-consuming sweeps, and live provider reads; prefer stored reads and dry-run previews where available.

## Reference(s):

- [ClawHub Canonry Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis](references/aeo-analysis.md)
- [Indexing Workflows](references/indexing.md)
- [Server-side Traffic](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and structured-data snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a separately installed Canonry npm runtime and should avoid exposing secrets or raw credentials in chat, logs, or shell history.]

## Skill Version(s):

4.183.0+885686f (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
