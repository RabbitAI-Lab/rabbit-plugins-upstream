## Description:

Lead Magnet helps an agent turn supplied expertise materials into a grounded, askable digital-human free mini course for list building.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and their agents use this skill to create an interactive lead magnet mini course from supplied source materials. The workflow supports grounded course planning, PersonWise CLI execution, review checkpoints, and access or publication steps requested by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a local PersonWise executable and use browser OAuth.

Mitigation: Install only if the user trusts PersonWise, require explicit approval for installation or update actions, and use browser OAuth without requesting passwords, tokens, cookies, or secrets.

Risk: The workflow may upload user-named materials and use existing course credits.

Mitigation: Upload only materials named or explicitly selected by the user, create only the requested number of courses, and require new approval for payments, additional courses, broader visibility, deletion, transfer, or organization administration.

Risk: Marketing course output could include unsupported claims if it drifts from the supplied materials.

Mitigation: Keep claims evidence-locked to the supplied materials, avoid fake scarcity and guaranteed outcomes, and review course checkpoints for factual support before delivery.

## Reference(s):

- [Lead Magnet ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-lead-magnet)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)
- [PersonWise service](https://personwise.ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create bounded local JSON blueprint files and issue PersonWise CLI commands that return structured JSON.]

## Skill Version(s):

2.1.9 (source: server release evidence and skill invocation attribution)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
