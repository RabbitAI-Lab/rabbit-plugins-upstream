## Description:

Queries Zhihuiya (PatSnap) patent legal status data to help users check patent validity, lifecycle status, and legal event history by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Patent professionals, developers, and external users use this skill to query one or more patents for current legal standing, detailed lifecycle status, and events such as transfers, licenses, pledges, litigation, invalidation, or re-examination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox and PatSnap network services and may handle sensitive patent, account, API key, and billing information.

Mitigation: Install and run it only when those services are acceptable for the task, avoid sharing confidential patent or business information unnecessarily, and review API key handling before use.

Risk: The onboarding helper can guide SMS login, expose an API key in command output, and create paid order flows.

Mitigation: Use authentication and payment helpers only after explicit user intent, and confirm plan and payment choices before creating an order.

Risk: The skill stores complete lookup responses locally and includes automatic feedback reporting instructions.

Mitigation: Review local saved response files for sensitive content and disable or review feedback reporting before using the skill with confidential material.

## Reference(s):

- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-legal-status)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance, JSON files]

**Output Format:** [Markdown guidance with structured tables, API response summaries, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The lookup script stores full responses under a local linkfox directory; large responses are summarized unless inline output is explicitly requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
