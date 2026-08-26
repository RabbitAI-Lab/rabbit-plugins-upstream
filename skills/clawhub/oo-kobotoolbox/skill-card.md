## Description:

Use this skill to operate KoboToolbox through an OOMOL-connected account for reading, creating, updating, exporting, validating, and deleting survey projects and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent work with KoboToolbox survey assets, form submissions, exports, deployments, validation status, and deletion tasks through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing KoboToolbox actions can create projects, deploy or redeploy forms, start exports, or change submission validation status.

Mitigation: Confirm the exact action, target project or submission, and payload with the user before running write actions.

Risk: Destructive submission deletion can remove real KoboToolbox data.

Mitigation: Require explicit user approval for the specific submission before running delete_submission.

Risk: Exports and submission reads may expose survey response data.

Mitigation: Use the skill only with the intended OOMOL-connected KoboToolbox account and review export or download requests before approval.

## Reference(s):

- [ClawHub KoboToolbox Skill Page](https://clawhub.ai/oomol/skills/oo-kobotoolbox)
- [KoboToolbox Homepage](https://www.kobotoolbox.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent fetches live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
