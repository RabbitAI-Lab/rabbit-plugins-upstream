## Description:

Builds, reviews, and troubleshoots Sendly welcome, drip, and onboarding email workflows, creating new workflows disabled by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Teams managing lifecycle email use this skill to create disabled onboarding workflows, review existing sequences, diagnose delivery problems, and propose approved changes in Sendly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabling or changing a live workflow can send unintended email to real contacts.

Mitigation: Review triggers, email steps, templates, and workflow names before approving; require explicit approval before enabling or editing a live workflow.

Risk: Deleting a workflow can remove an active automation.

Mitigation: Confirm the workflow by name and require explicit approval before deletion.

## Reference(s):

- [Sendly: Building Onboarding Workflows on ClawHub](https://clawhub.ai/bsalaeddin/skills/sendly-building-onboarding-workflows)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes workflow triggers, steps, status, and troubleshooting findings; new workflows remain disabled pending explicit approval to enable.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
