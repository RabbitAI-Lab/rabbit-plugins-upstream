## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing or SEO teams use Canonry to review AI-visibility and website evidence, diagnose changes, plan measurement, manage integrations, and prepare reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis may expose project or visitor data, and connected integrations may use sensitive credentials.

Mitigation: Prefer stored-only analysis with project-scoped read credentials, and keep credentials out of chat.

Risk: Website edits, paid runs, advertising activation, or recurring work can have consequential side effects.

Mitigation: Obtain separate approval for each consequential change or paid or recurring action.

Risk: Traffic integrations process visitor request data, and removed Cloudflare integrations may leave dedicated tokens or local credentials.

Mitigation: Handle visitor data carefully; when removing Cloudflare integration, revoke dedicated tokens and clean up retained local credentials.

## Reference(s):

- [Canonry on ClawHub](https://clawhub.ai/arberx/skills/canonry)
- [AEO Analysis Guide](artifact/references/aeo-analysis.md)
- [Canonry CLI Reference](artifact/references/canonry-cli.md)
- [Google Business Profile Reference](artifact/references/google-business-profile.md)
- [Google Marketing Reference](artifact/references/google-marketing.md)
- [Indexing Guide](artifact/references/indexing.md)
- [Server-Side Traffic Guide](artifact/references/server-side-traffic.md)
- [WordPress Integration Guide](artifact/references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions depend on connected tools and user approval.]

## Skill Version(s):

7.51.0+2694af8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
