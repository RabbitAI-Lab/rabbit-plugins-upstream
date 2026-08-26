## Description:

Operate Canonry for AEO workflows, including project setup, integrations, sweeps, audits, indexing, mention and citation coverage, traffic sources, and related CLI or MCP operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing engineers use this skill to operate Canonry's AEO platform from an agent, including measuring AI answer-engine mentions and citations, diagnosing visibility changes, configuring integrations, and preparing guarded operational actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured Canonry key may let an agent read or mutate projects and shared instance settings within that key's server-enforced scope.

Mitigation: Install only when agent operation of Canonry is intended; prefer read-only or project-scoped keys and do not switch credentials to bypass missing tools or authorization failures.

Risk: Canonry integrations can involve API keys, OAuth tokens, and integration credentials stored in the local Canonry configuration.

Mitigation: Protect ~/.canonry/config.yaml, avoid printing or pasting credentials, and ask the operator to complete credentialed initialization in a private terminal.

Risk: Sweeps, live provider reads, writes, schedules, and traffic operations can consume quota or change connected systems.

Mitigation: Require explicit operator approval before each mutation, quota-consuming sweep, live provider read, or live WordPress action; use stored reads and dry-run previews where available.

## Reference(s):

- [Canonry Skill](SKILL.md)
- [Canonry CLI Reference](references/canonry-cli.md)
- [AEO Analysis](references/aeo-analysis.md)
- [Indexing Workflows for AEO](references/indexing.md)
- [Server-side Traffic](references/server-side-traffic.md)
- [Google Business Profile Integration](references/google-business-profile.md)
- [Google Ads and Google Tag Manager](references/google-marketing.md)
- [WordPress Integration](references/wordpress-integration.md)
- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown guidance with inline CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose reads, writes, live provider checks, sweeps, or schedules; quota-consuming or mutating actions should remain operator-approved.]

## Skill Version(s):

4.177.2+2e38f1d (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
