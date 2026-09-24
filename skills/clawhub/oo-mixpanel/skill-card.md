## Description:

Operate Mixpanel through an OOMOL-connected account with the oo CLI for reading, creating, updating, querying, and exporting Mixpanel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to run Mixpanel connector actions, inspect live action schemas, query saved reports and behavioral analytics, export events, and handle account setup or billing errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unpinned remote shell installers.

Mitigation: Review the oo CLI installer before running it, or prefer a package-manager or verified installer path when available.

Risk: The connector can access Mixpanel analytics data, including raw events and profile information, through an OOMOL-connected account.

Mitigation: Install and use the skill only when that account-level Mixpanel access is acceptable, and confirm state-changing payloads before running actions tagged as write or destructive.

## Reference(s):

- [Mixpanel homepage](https://mixpanel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mixpanel)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
