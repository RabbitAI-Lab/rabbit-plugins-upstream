## Description:

Creates reviewable Google Ads search campaign plans from JSON specs and, with explicit approval, creates campaigns in a paused state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers and campaign managers use this skill to draft and review search campaign specifications before a human approves creation of a paused campaign.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying a campaign accesses the target Google Ads account and can create a campaign.

Mitigation: Review the offline plan before using --apply, restrict OAuth credentials to the intended account, and confirm the created campaign remains paused.

Risk: The optional budget-cap automation can pause live campaigns or leave other campaigns spending.

Mitigation: Have a human scope, install, and monitor the separate script; verify its campaign-name filter and account-level cap before enabling pauses.

## Reference(s):

- [Google Ads Campaigns as Code on ClawHub](https://clawhub.ai/alexbloch-ia/skills/google-ads-campaigns)

## Skill Output:

**Output Type(s):** [JSON specifications, Text campaign plans, Shell commands, Code]

**Output Format:** [JSON campaign specs and human-readable campaign plans with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Campaign creation requires explicit approval and leaves the campaign paused.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
