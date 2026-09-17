## Description:

PostHog lets an agent read, create, update, and delete PostHog resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and analytics teams use this skill to manage PostHog projects, dashboards, insights, cohorts, annotations, feature flags, event definitions, and property definitions through the OOMOL PostHog connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify PostHog resources, including destructive operations such as deletes and collaborator removal.

Mitigation: Grant access only when the user is comfortable with that authority, and require explicit confirmation of targets and payloads before write or destructive actions.

Risk: Security evidence reports that setup instructions can run an unverified remote installer.

Mitigation: Avoid pipe-to-shell installation unless the installer source, checksum, signature, and expected behavior are verified through a trusted channel.

Risk: Security evidence reports that dashboard reordering is a dashboard-changing action mislabeled as safe.

Mitigation: Manually confirm dashboard reordering requests before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-posthog)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [PostHog homepage](https://posthog.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL PostHog connection](https://console.oomol.com/app-connections?provider=posthog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the OOMOL PostHog connector.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
