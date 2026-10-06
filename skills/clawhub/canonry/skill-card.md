## Description:

Guides agents using Canonry MCP tools or the optional CLI to inspect evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to navigate Canonry, interpret stored visibility evidence, diagnose changes, plan measurements, and review approved integrations and operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad business and marketing administration workflows may change live projects or connected providers.

Mitigation: Require explicit approval for writes, provider syncs, ads changes, webhook setup, and schedules; check the exact target and scope first.

Risk: Credentials and token files used for Canonry operations may be exposed.

Mitigation: Use project-scoped keys where possible, keep Canonry configuration and tokens private, and never paste secrets into chat.

Risk: Telemetry or feedback submission may share operational information.

Mitigation: Obtain explicit approval before telemetry or feedback submission.

## Reference(s):

- [Canonry skill on ClawHub](https://clawhub.ai/arberx/skills/canonry)
- [Canonry CLI commands and results](references/canonry-cli.md)
- [Interpreting visibility evidence](references/aeo-analysis.md)
- [Indexing workflow](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic](references/server-side-traffic.md)
- [Google Business Profile](references/google-business-profile.md)
- [Google Ads and Tag Manager](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on connected tools, project access, and operator approval.]

## Skill Version(s):

7.2.0+fd79321 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
