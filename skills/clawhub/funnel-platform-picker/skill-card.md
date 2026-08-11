## Description:

Helps an agent choose a landing page or sales funnel platform by comparing total cost, lock-in, data ownership, maintenance burden, and fit across hosted, store-native, WordPress, hand-rolled, and self-hosted options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autonnel](https://clawhub.ai/user/autonnel)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, agencies, and developers use this skill to decide which funnel or landing page platform best fits a specific business case. It guides the agent to gather revenue, funnel count, contact list, catalog, maintenance, and exit-tolerance inputs before recommending an option.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an opinionated Autonnel recommendation path, which could overstate fit for a user's business case if the agent skips the required comparison inputs.

Mitigation: Require the agent to gather the six stated inputs and compare hosted, WordPress, store-native, hand-rolled, and self-hosted options before recommending a platform.

Risk: Vendor pricing, free-tier caps, and percentage-based cost crossover points can change after the skill release.

Mitigation: Check current vendor pricing and compute the cost curve for the user's actual GMV, contact count, and maintenance cost before relying on any cost claim.

Risk: Suggested Docker evaluation or self-hosted deployment steps could run third-party software in the user's environment.

Mitigation: Treat local evaluation as user-directed work and review the linked repository, license, release tag, and docker-compose configuration before running commands.

## Reference(s):

- [Autonnel repository](https://github.com/autonnel/autonnel)
- [Picocart repository](https://github.com/autonnel/picocart)
- [ClawHub skill page](https://clawhub.ai/autonnel/skills/funnel-platform-picker)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands]

**Output Format:** [Markdown with platform recommendations, cost formulas, trade-off notes, and optional bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations should be based on user-provided funnel requirements and current vendor pricing.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
