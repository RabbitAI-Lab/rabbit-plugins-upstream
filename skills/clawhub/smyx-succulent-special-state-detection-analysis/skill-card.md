## Description:

Analyzes succulent images or videos to identify black rot, water-soaked leaves, or stretching and report severity and confidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home growers, succulent greenhouses, and flower shops use the skill to screen plant images or videos for black rot, water-soaked leaves, and stretching, with severity and confidence estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports automatic account creation and unsafe credential handling.

Mitigation: Wait for fixes before installing; if evaluating, use an isolated workspace and non-sensitive plant media.

Risk: Images and videos leave the device, and report retention and deletion details are not established in the supplied guidance.

Mitigation: Use non-sensitive plant media and ask the publisher about report retention and deletion.

Risk: The security review reports that an option intended to prevent analysis is ignored.

Mitigation: Do not rely on that option to prevent analysis; wait for a fix before installing.

## Reference(s):

- [Succulent analysis API documentation](references/api_doc.md)
- [API response and error documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis report with detected condition, severity, confidence, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts plant images or videos; visual assessments may be uncertain.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
