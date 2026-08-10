## Description:

Analyzes infant diaper or stool images and URLs through a cloud health-analysis service to classify stool color, flag clay-pale or bloody/tarry appearances, and return risk guidance with report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and infant-care workflows use this skill to submit diaper or stool imagery for visual color screening and receive structured risk reminders. It supports new-parent, pediatric clinic, postpartum care, and smart infant-care device scenarios, but its output is only screening guidance and not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant diaper or stool images, URLs, metadata, and report queries may be sent to configured cloud services.

Mitigation: Use only with explicit guardian consent, approved cloud endpoints, and clear retention and deletion expectations.

Risk: The skill silently creates or reuses account identity and can store tokens locally.

Mitigation: Review identity and token storage behavior before installation, and run only in environments where silent account management is acceptable.

Risk: Network URL inputs could expose private-network or unrelated resources to the service.

Mitigation: Provide only intended public image URLs or vetted local files, and avoid private-network URLs.

Risk: Visual color screening can be affected by lighting, filters, image quality, or medical context outside the image.

Mitigation: Treat outputs as screening guidance, retake poor-quality images in neutral light, and route abnormal or uncertain results to qualified pediatric care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Infant stool color API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured report text or JSON, with Markdown tables for history listings and report export links when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include color classification, risk level, confidence, recommended action, alert text, and cloud report links.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
