## Description:

Checks relaunch readiness risk for an existing Amazon ASIN using product details and existing review evidence; requires an existing ASIN, at least 10 reviews, and an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to assess whether an existing ASIN is ready for a listing refresh or relaunch. It checks product details and review evidence, then surfaces readiness risks, data gaps, and action recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is presented as a launch-readiness checker, while security evidence says artifacts expose broader account, billing, monitoring, export, and paid-analysis actions.

Mitigation: Install only if the broader ARI account-connected assistant behavior is acceptable, and review available actions before enabling the skill.

Risk: The skill stores and uses an ARI API key and may run paid analyses under server-side auto-confirm rules.

Mitigation: Complete authorization in the browser, do not paste API keys into chat, and set auto-confirm to always ask before paid actions if cost control is required.

Risk: Recurring monitoring, collection schedules, and competitor tracking can create ongoing account activity and future costs.

Mitigation: Enable recurring actions only after explicit consent and cost review; use manual, pause, or delete controls when monitoring is no longer wanted.

Risk: Interrupted paid operations may already have consumed credits or produced an archived report.

Mitigation: Check the relevant report or operation status using the original ASIN or request ID before retrying a paid command.

## Reference(s):

- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [User guide](artifact/使用说明.md)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/launch-readiness)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands and links to generated reports or exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish direct data, interpretation, and recommendations; report scope, sample size, usage, and limitations when evidence is incomplete.]

## Skill Version(s):

1.4.8 (source: frontmatter, release evidence, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
