## Description:

Navigate Canonry through connected MCP tools or the `cnry` CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results. Use this optional host-native skill for CLI workflows and detailed references; connected MCP users can operate through canonry_help without installing a local runtime or skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Canonry-connected agents to inspect stored website and AI-visibility evidence, diagnose issues, plan measurements, review integrations, and report results. The guide helps them choose MCP or `cnry` CLI workflows while keeping approval boundaries explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis may be incomplete or misleading if project scope, time window, provider, or sample details are missing or incomparable.

Mitigation: Use project-scoped read-only access and stored-only mode; preserve the scope and time details of evidence and state when evidence is missing.

Risk: Production changes, advertising budgets, recurring schedules, or feedback can have consequential or paid effects.

Mitigation: Review exact proposed changes and bounds, and obtain authorized approval before execution.

Risk: Traffic collection can transmit sensitive URL and visitor details to a configured receiver.

Mitigation: Confirm the receiver and its handling of URL and visitor data before enabling collection.

Risk: Cloudflare credentials may remain in local storage after use.

Mitigation: Use dedicated Cloudflare tokens, revoke them, and remove retained local credentials during teardown.

## Reference(s):

- [Canonry ClawHub release](https://clawhub.ai/arberx/skills/canonry)
- [AEO Analysis: Interpreting Canonry Results](references/aeo-analysis.md)
- [Canonry CLI](references/canonry-cli.md)
- [Google Business Profile](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side traffic](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and reports, with shell commands and configuration examples where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and external actions remain subject to the documented approval boundaries.]

## Skill Version(s):

7.50.1+a36190c (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
