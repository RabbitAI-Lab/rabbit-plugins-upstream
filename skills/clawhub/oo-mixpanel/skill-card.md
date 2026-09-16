## Description:

Mixpanel (mixpanel.com). Use this skill for ANY Mixpanel request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Mixpanel data through an OOMOL-connected account, including raw event exports, profiles, cohorts, funnels, retention, segmentation, saved reports, and top-event analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Prefer a verified package-manager or signed installer path, and inspect installer contents before execution.

Risk: Mixpanel event and profile exports can contain sensitive customer or product analytics data.

Mitigation: Limit access to trusted workspaces, avoid unnecessary raw exports, and handle returned data according to the user's data handling policy.

Risk: The skill operates through OOMOL as an intermediary for Mixpanel access.

Mitigation: Install only when the user trusts OOMOL with the connected Mixpanel account and accepts the server-side credential flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mixpanel)
- [Mixpanel](https://mixpanel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Mixpanel query results returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
