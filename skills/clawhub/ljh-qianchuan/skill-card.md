## Description:

ljh-qianchuan is a Douyin Qianchuan ad traffic-drop diagnostic skill that guides users through a decision tree to identify likely causes and first corrective actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and ad teams use this skill to diagnose Douyin Qianchuan traffic, spend, GMV, ROI, conversion, and fulfillment drops through a step-by-step triage flow. It helps narrow symptoms to account, creative, livestream conversion, audience, fulfillment, or external-market factors and then proposes a first action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a first-use marker in the user's home directory.

Mitigation: Install and run it only when that persistence is acceptable, or instruct the agent not to create onboarding state.

Risk: The skill may read and update a local brand archive and save diagnostic outputs for reuse.

Mitigation: Use it in a dedicated project folder and opt out of archive creation or updates when persistent business records are not desired.

Risk: The skill displays WeChat contacts for off-platform support.

Mitigation: Treat those contacts as optional support information and do not consider them required for the diagnostic workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-qianchuan)
- [Publisher profile](https://clawhub.ai/user/handsomeng)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Files]

**Output Format:** [Conversational Markdown with diagnostic questions, conclusions, and optional local archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create an onboarding marker in the user's home directory and may read or update a local brand archive when the user allows persistent records.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
