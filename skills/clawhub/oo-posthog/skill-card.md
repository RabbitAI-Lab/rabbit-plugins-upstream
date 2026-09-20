## Description:

Operates PostHog through OOMOL's oo CLI so an agent can inspect schemas and read, create, update, or delete PostHog data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage PostHog dashboards, insights, cohorts, feature flags, annotations, event and property definitions, projects, collaborators, and queries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote installer scripts without verification.

Mitigation: Install the oo CLI manually from verified official instructions and review the installer path before execution.

Risk: The skill can execute write and destructive PostHog actions.

Mitigation: Use a least-privilege PostHog connection where possible and require explicit review before any write or destructive action.

Risk: Use depends on trusting OOMOL and the oo CLI installation path.

Mitigation: Decide whether OOMOL and the CLI distribution path are trusted before installing or using the connector.

## Reference(s):

- [ClawHub PostHog skill](https://clawhub.ai/oomol/skills/oo-posthog)
- [PostHog homepage](https://posthog.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and applies confirmation guidance for write or destructive PostHog operations.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
