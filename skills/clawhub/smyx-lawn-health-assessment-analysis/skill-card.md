## Description:

Assesses lawn images or videos for wilting, weeds, bare soil, and overall turf health, then provides care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Lawn and grounds managers, including golf course, municipal, sports field, and home users, can assess top-down lawn photos or videos. They use the resulting wilting, weed, bare-soil, and health estimates to guide routine irrigation, fertilization, weeding, or reseeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media may be uploaded to the analysis service even when using the configuration-only option.

Mitigation: Assume media is transmitted until the publisher clarifies the behavior and retention policy; use nonsensitive images and a dedicated service account for evaluation.

Risk: Configured secrets may be mishandled, and credentials may be retained.

Mitigation: Keep API secrets separate from account identifiers, and ask the publisher to explain account creation and token removal before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured lawn assessment results, with Markdown tables for report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wilting, weed, and bare-soil ratios, a health score, care-direction suggestions, and report links. Treat visual estimates as decision support.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
