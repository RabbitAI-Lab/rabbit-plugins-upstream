## Description:

Assesses ornamental fish color brightness from images or video and provides a vibrancy report with husbandry guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium owners, fish farms, and aquatic-care teams use the skill to review fish color trends from images or video and receive assessment reports and care suggestions; it is not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images or videos are sent to the publisher's cloud service.

Mitigation: Obtain informed consent before sending media and confirm the publisher's retention and sharing terms.

Risk: The skill creates or reuses a local identity record and caches service tokens without a prominent user prompt.

Mitigation: Disclose the identity and token handling, restrict local access, and define storage limits and deletion procedures.

Risk: The analysis may not reliably deliver the advertised fish-specific assessment.

Mitigation: Check reports against the supplied images and species information; do not use scores as a veterinary diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or JSON report with optional Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a historical report list and save results to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
