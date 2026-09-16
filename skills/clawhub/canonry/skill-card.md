## Description:

Canonry guides agents through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing analysts use this skill to work with Canonry projects, review stored AI visibility evidence, diagnose measurement changes, plan approved operations, and prepare reports without treating the skill itself as an authorization mechanism.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented workflows can involve broad authority, persistent credentials, and raw visitor data.

Mitigation: Install only if the publisher is trusted, keep credentials narrowly scoped where possible, protect `~/.canonry/config.yaml`, and require explicit approval before writes, syncs, deployments, provider calls, or recurring schedules.

Risk: Provider credentials and API keys could be exposed through chat, command lines, logs, or public guidance.

Mitigation: Use secure setup flows for credentials, avoid pasting secrets into agent conversations or shell commands, and prefer read-only or narrowly scoped keys.

Risk: Cloudflare direct-push traffic workflows can have privacy implications when routing production traffic.

Mitigation: Review the direct-push data path and privacy impact before enabling it for production traffic.

## Reference(s):

- [Canonry Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Google Marketing Setup Guide](https://github.com/Canonry/canonry/blob/main/docs/google-marketing.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, analysis]

**Output Format:** [Markdown with inline command examples and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference connected MCP tools, Canonry CLI commands, and project-specific evidence; operator approval is needed before writes, syncs, provider calls, deployments, recurring schedules, or externally visible actions.]

## Skill Version(s):

5.3.0+caba5d3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
