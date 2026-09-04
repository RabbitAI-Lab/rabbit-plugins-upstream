## Description:

Operate Canonry (`cnry` / `canonry`) for Answer Engine Optimization workflows, including brand visibility sweeps, technical audits, indexing, traffic integrations, Google marketing reads, and guarded reporting or content actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and site operators use this skill to run Canonry-backed AEO operations: measure AI answer mentions and citations, diagnose visibility gaps, inspect connected analytics and marketing evidence, and apply approved fixes through the Canonry CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through workflows that access sensitive website, marketing, traffic, and provider accounts.

Mitigation: Use scoped or read-only keys when possible, keep service credentials local, and protect ~/.canonry/config.yaml.

Risk: Some Canonry operations can mutate projects, schedules, WordPress content, ads state, or consume paid provider quota.

Mitigation: Require explicit approval before writes, schedules, sweeps, ads actions, and live provider reads; use supported dry-run modes before committing changes.

Risk: Generated AEO recommendations may misstate mention, citation, indexing, or traffic evidence if stale or incomplete data is treated as final.

Mitigation: Prefer stored evidence for routine reads, keep provider and model choices explicit, and report uncertainty when a sweep, sync, or live read has not been run.

## Reference(s):

- [Canonry skill page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry website](https://canonry.ai)
- [Canonry repository](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis](references/aeo-analysis.md)
- [Indexing Workflows](references/indexing.md)
- [Server-Side Traffic](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a separately installed Canonry CLI/daemon and local service credentials for connected providers.]

## Skill Version(s):

4.180.2+5b70be1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
