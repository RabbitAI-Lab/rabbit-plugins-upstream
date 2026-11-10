## Description:

AI-powered lawn health assessment from drone or fixed-camera top-down images. Uses semantic segmentation to distinguish healthy turf, wilting or yellow turf, bare soil, and weeds, then computes wilting and weed coverage ratios and a composite lawn health score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External grounds managers can use this skill to assess lawn images or videos, quantify wilting, weeds, and bare soil, and guide irrigation, fertilization, or weeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports account and credential handling, remote identity transmission, and media upload behavior whose fit with lawn analysis is unclear.

Mitigation: Review what identity and image data the skill sends and retains, and submit only information and media you are authorized to share.

Risk: The security review says scanner coverage was partial because one local reference was missing, so its assessment is incomplete.

Mitigation: Review the complete package and referenced materials before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured lawn assessment report with ratios, health score, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include lawn condition metrics and maintenance guidance derived from the submitted image or video.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
