## Description:

Cross-vendor adversarial review of plans, proposals, or designs by sending a prepared brief to a different vendor's model for attack, defense, and final consensus.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user explicitly requests cross-vendor adversarial review of a plan, proposal, or design before acting on it. It structures the review into a prepared brief, external attack, local defense, final consensus, and optional fresh-session judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The prepared debate brief is sent verbatim to the selected external model or vendor.

Mitigation: Remove secrets, credentials, regulated personal data, proprietary source excerpts, and internal-only details unless they are approved for that vendor.

Risk: External model or handoff backend configuration may have data-retention or access rules that differ from the local environment.

Mitigation: Confirm the selected channel and backend configuration match organizational data-retention and access requirements before use.

Risk: Adversarial objections or consensus items can contain incorrect citations, assumptions, or recommendations.

Mitigation: Spot-check cited files and line numbers, keep defense and rulings in the main session, and require user confirmation before applying any outcome.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/adversarial-debate)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and consensus lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces candidate review outcomes only; user confirmation is required before any decision or implementation proceeds.]

## Skill Version(s):

2.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
