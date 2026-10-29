## Description:

Identifies bird species in images or videos and returns structured recognition results for ecological observation and birdwatching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit bird images or videos for species identification and review structured results. Developers can also use it to retrieve historical recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports silent account creation and persistence of sensitive account data.

Mitigation: Wait for explicit account-binding controls and protected credential storage; use a separate workspace and dedicated credentials when evaluating the skill.

Risk: Images and videos are sent to LifeEmergence cloud services, and retention terms have not been verified.

Mitigation: Avoid submitting private footage until the service's retention terms are verified.

Risk: The security review reports that the option intended to prevent analysis is ignored.

Mitigation: Wait until the non-execution option is confirmed to work before relying on it.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Sample skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Structured recognition report in JSON or text, with Markdown presentation available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include species classifications, confidence scores, recommendations, and report links.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
