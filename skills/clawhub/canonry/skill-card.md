## Description:

Guides agents using Canonry MCP tools or the optional CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and agents use Canonry to review stored AI visibility and site evidence, investigate changes, plan measurement, and prepare integrations or reports. Live provider actions and site changes require operator approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live provider reads and syncs can consume quotas or change stored evidence.

Mitigation: Prefer stored reads; get approval for the exact target and bounded live operation before proceeding.

Risk: Site edits, deployments, schedules, webhooks, and traffic instrumentation can have externally visible effects.

Mitigation: Review the proposed change and require explicit operator approval before writes or deployment.

Risk: API keys and OAuth tokens can be exposed in chat, reports, or local configuration files.

Mitigation: Keep secrets out of chat and reports; protect local Canonry configuration and token files.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](artifact/references/canonry-cli.md)
- [Interpreting AI visibility evidence](artifact/references/aeo-analysis.md)
- [Indexing workflows](artifact/references/indexing.md)
- [WordPress integration](artifact/references/wordpress-integration.md)
- [Server-side traffic setup](artifact/references/server-side-traffic.md)
- [Google Business Profile prerequisites](artifact/references/google-business-profile.md)
- [Google marketing evidence boundaries](artifact/references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown and plain text, with commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should distinguish stored evidence from unverified hypotheses and identify actions requiring approval.]

## Skill Version(s):

7.44.0+89a7b4b (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
