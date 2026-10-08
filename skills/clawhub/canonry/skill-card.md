## Description:

Guides agents through Canonry's connected tools or CLI to inspect AI visibility evidence, diagnose changes, plan measurement, review integrations, and report results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and operators use this skill to inspect Canonry projects, interpret AI visibility measurements, plan approved actions, and review integrations through connected tools or optional CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative actions can change projects, schedules, ads, WordPress content, or public indexing state.

Mitigation: Inspect the proposed scope and require explicit operator approval before writes, syncs, or public-facing changes.

Risk: Provider calls and measurement runs may consume quota or incur spend.

Mitigation: Confirm the selected project, providers, queries, and cost-bearing action before execution.

Risk: Exposing credentials could grant access to Canonry or connected providers.

Mitigation: Keep API keys, OAuth secrets, tokens, and application passwords out of chat; protect local configuration and prefer narrow, project-scoped read-only keys.

## Reference(s):

- [Canonry skill release](https://clawhub.ai/arberx/skills/canonry)
- [CLI commands and JSON return shapes](references/canonry-cli.md)
- [Interpreting stored evidence and regressions](references/aeo-analysis.md)
- [Indexing workflows](references/indexing.md)
- [WordPress integration](references/wordpress-integration.md)
- [Server-side traffic setup and diagnosis](references/server-side-traffic.md)
- [Google Business Profile prerequisites](references/google-business-profile.md)
- [Google Ads and Tag Manager evidence boundaries](references/google-marketing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations distinguish stored evidence from unverified hypotheses and approval-gated actions.]

## Skill Version(s):

7.11.0+df2022e (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
