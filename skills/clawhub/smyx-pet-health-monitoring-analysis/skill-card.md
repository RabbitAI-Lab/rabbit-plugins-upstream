## Description:

Based on computer vision, this skill analyzes pet feeding, drinking, excretion, mental state, vomiting, and limping signals from camera or feeder monitoring media and outputs health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care developers use this skill to submit pet monitoring videos or URLs for computer-vision-based health behavior analysis and structured reporting. It can also query cloud-hosted historical pet health monitoring reports associated with the internally resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet-monitoring media and report history may be sent to the publisher's backend.

Mitigation: Use only with media and report data you are comfortable sharing with the publisher, and confirm data-handling expectations before routine use.

Risk: Release security guidance flags non-HTTPS endpoints, development defaults, silent account creation, and reusable token handling as issues to resolve before routine use.

Mitigation: Ask the publisher to use HTTPS-only release endpoints, remove development defaults, avoid silent account creation, and store reusable tokens in a proper secret store.

Risk: Pet health analysis reports are advisory and do not replace professional veterinary diagnosis.

Mitigation: Treat the output as health-monitoring guidance and consult a veterinarian for concerning symptoms or abnormal behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet health API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON health monitoring report with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured health indicators, abnormality warnings, care suggestions, and cloud report export URLs.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
