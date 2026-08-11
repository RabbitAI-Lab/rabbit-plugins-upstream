## Description:

Customer Onboarding Course helps agents create grounded interactive digital-human onboarding courses from confirmed customer onboarding materials, with learner voice questions and optional assessments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer success and implementation teams use this skill to turn confirmed onboarding materials into an interactive course for new customers. The course stays grounded in supplied evidence for scope, commitments, timelines, support channels, visuals, and learner questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or update the PersonWise CLI and uses browser OAuth.

Mitigation: Review host approval prompts carefully, use only the official bundled PersonWise CLI and declared service, and never provide passwords, tokens, cookies, or authorization secrets to the agent.

Risk: Selected onboarding materials may be uploaded to PersonWise to create the course.

Mitigation: Upload only files the user named, attached, or explicitly selected; require approval for agent-discovered local files; never expose upload grants, signed URLs, or private source contents.

Risk: Course creation can consume existing credits or broaden access if link access or publication is requested.

Mitigation: Create only the requested number of courses, never buy credits automatically, default unspecified distribution to private, and change access only when requested.

Risk: Unsupported onboarding promises could mislead learners about scope, timelines, SLAs, pricing, or contacts.

Mitigation: Use confirmed source material only, omit unverified claims, and route customer-specific contract or plan questions back to the user's team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-customer-onboarding)
- [PersonWise service](https://personwise.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON blueprint inputs, shell commands, and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create PersonWise course artifacts and return run/project IDs plus the correct private or share URL when fresh state proves playability.]

## Skill Version(s):

2.1.9 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
