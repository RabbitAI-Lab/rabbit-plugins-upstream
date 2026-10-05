## Description:

Builds a grouped account report from a supplied reporting recipe.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to group and summarize account records according to a supplied reporting recipe.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured external delivery target can receive report data automatically without per-run confirmation.

Mitigation: Keep delivery environment variables unset for local-only use; review any configured delivery destination before running.

## Reference(s):

- [Account Group Report Builder on ClawHub](https://clawhub.ai/wxt-ai/skills/account-group-report-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON report with a local report artifact and optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes report ID, groups, row count, and projected columns.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
