## Description:

Ironheights helps users review skills for suspicious content and monitor approved skills for security drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Ironheights to scan skills before trusting them, check for changes after approval, and review repository threat-model findings. It provides advisory results and user-controlled next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hostile skill could try to manipulate an agent that is reviewing it.

Mitigation: Run the review outside the agent or use another independent process.

Risk: The npm CLI is outside the inspected artifact, so its behavior is not covered by this artifact's scan evidence.

Mitigation: Review the publisher source and verify the CLI package before installing it.

Risk: Optional model review can transmit skill text to a server.

Mitigation: Keep model review off unless the user explicitly chooses to send the skill text.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands]

**Output Format:** [Markdown guidance with findings and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results and user-controlled next steps.]

## Skill Version(s):

1.8.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
