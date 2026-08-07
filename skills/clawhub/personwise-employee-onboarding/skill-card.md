## Description:

Creates a grounded interactive digital-human new-hire onboarding course from supplied handbooks, onboarding plans, and internal documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and people teams use this skill to create a source-grounded interactive digital-human onboarding course from handbooks, onboarding plans, and internal documentation. It is intended for new-hire onboarding and role ramp, not customer onboarding, partner onboarding, performance management, or HR case handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses PersonWise's hosted service and can upload selected onboarding materials.

Mitigation: Install and use it only when uploading the chosen materials to PersonWise is acceptable; keep the course private unless broader access was explicitly requested.

Risk: The workflow requires browser OAuth and account-bound course creation.

Mitigation: Use the browser OAuth flow and do not provide passwords, tokens, cookies, authorization codes, or other secrets to the agent.

Risk: The skill may install or update the PersonWise CLI in the user's profile.

Mitigation: Review host install or update approval prompts carefully and approve only the intended PersonWise CLI action.

Risk: Course creation can consume existing PersonWise course credits and some actions can broaden sharing or affect account resources.

Mitigation: Do not approve payments, broader sharing, deletion, transfers, or organization administration unless that action was intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/personwiseai/skills/personwise-employee-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with CLI commands and bounded JSON inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return course run identifiers, project identifiers, source statuses, review results, access state, and the appropriate course URL.]

## Skill Version(s):

2.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
