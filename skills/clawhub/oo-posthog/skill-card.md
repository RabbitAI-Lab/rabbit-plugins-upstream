## Description:

This skill lets agents use PostHog for reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate PostHog through an OOMOL-connected account, including reading, creating, updating, and deleting PostHog projects, dashboards, insights, cohorts, annotations, feature flags, event definitions, and property definitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, modify, and delete PostHog resources through an OOMOL-connected account.

Mitigation: Install only when OOMOL is trusted, confirm write payloads before execution, and require explicit approval before destructive actions.

Risk: Fallback setup instructions include remote installer pipelines for the oo CLI.

Mitigation: Prefer a verified, pinned, or package-manager installation path before using the skill.

## Reference(s):

- [PostHog homepage](https://posthog.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-posthog)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before sending JSON payloads through the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
