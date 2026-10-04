## Description:

Analyzes infant diaper or stool images to classify stool color, flag potentially concerning results, and offer guidance on seeking medical care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and pediatric teams use the skill for preliminary review of infant stool color in diaper or stool images, with risk alerts and access to prior reports. Results are screening guidance, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant diaper or stool images and report history are sent to configured cloud services.

Mitigation: Obtain guardian consent and review cloud data retention and deletion before use.

Risk: The skill automatically creates or reuses a local identity with stored tokens.

Mitigation: Review local credential storage and limit access to the device and associated report history.

Risk: Broad triggers can start a cloud history lookup without explicit user confirmation.

Mitigation: Require confirmation before retrieving historical reports; prefer a release with narrower triggers.

Risk: Image-based screening can misclassify colors or fail to provide reliable medical guidance.

Mitigation: Use suitable lighting and seek prompt pediatric evaluation for concerning results rather than relying on the skill for diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [API interface and result fields](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or JSON; historical report listings may include Markdown links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stool-color categories, risk alerts, recommended actions, and report links.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
