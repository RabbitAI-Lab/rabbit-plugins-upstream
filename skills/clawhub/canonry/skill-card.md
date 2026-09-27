## Description:

Guides agents using Canonry MCP tools or the cnry CLI to inspect AI visibility evidence, diagnose changes, plan measurements, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use Canonry to review stored AI visibility measurements, investigate changes, plan approved measurement work, assess connected marketing integrations, and prepare evidence-based reports for their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or private project settings could be exposed during integration setup or diagnostics.

Mitigation: Keep API keys, OAuth secrets, application passwords, and Canonry configuration private; prefer read-only or project-scoped keys when possible.

Risk: Live provider calls and externally visible changes can consume quota or affect a site, ads, or recurring work.

Mitigation: Obtain explicit approval for the exact target and bounded action before live calls, site writes, ad activation, or schedules.

Risk: Incomplete or non-comparable evidence could lead to misleading visibility claims.

Mitigation: Use stored evidence first, keep mention and citation separate, and disclose dates, sample sizes, and missing or stale inputs.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI reference](artifact/references/canonry-cli.md)
- [AEO evidence and regression analysis](artifact/references/aeo-analysis.md)
- [Google marketing evidence boundaries](artifact/references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should distinguish mentions from citations and note missing or stale evidence.]

## Skill Version(s):

5.20.1+ce28687 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
