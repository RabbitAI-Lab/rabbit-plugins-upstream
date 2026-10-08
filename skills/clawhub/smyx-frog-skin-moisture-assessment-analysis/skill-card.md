## Description:

Assesses frog skin moisture from images or videos by examining glossiness, wrinkles, and whitish film, and provides dehydration-risk reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Frog keepers, amphibian breeders, and animal-care teams use the skill to review enclosure imagery for possible skin dryness, receive alerts, and consult historical assessment reports. Visual findings are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images, videos, or media URLs are sent to the LifeEmergence cloud service.

Mitigation: Obtain consent before uploading and avoid sensitive footage.

Risk: The skill may silently create or reuse an internal account and store authentication tokens locally.

Mitigation: Disclose the identity and token handling to users, obtain consent, and secure locally stored tokens before production use.

Risk: The reported import-path issue may prevent the skill from running as expected.

Mitigation: Fix the import path and test execution before production use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [Frog skin moisture assessment API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured assessment report, with optional saved file and historical report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes skin-condition observations, risk alerts, and suggested follow-up actions.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
