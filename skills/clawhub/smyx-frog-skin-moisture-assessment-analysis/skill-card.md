## Description:

Assesses frog skin moisture from dorsal or lateral images by analyzing glossiness and visible dryness cues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Frog keepers and animal care teams can use this skill to review dorsal or lateral frog images for skin moisture indicators, receive a structured assessment, and decide whether to check enclosure conditions or seek veterinary advice. It provides visual screening guidance rather than a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment says reports may be mixed across different users.

Mitigation: Have sender-specific account isolation fixed and verified before shared-agent use, and confirm report ownership before relying on results.

Risk: Selected media may be sent to a remote service, including when the export-only option is selected.

Mitigation: Confirm which images or videos leave the device and review service access, retention, deletion, and charges before submitting sensitive media.

Risk: The security guidance says API secrets may be exposed through profile fields and protected credential storage needs review.

Mitigation: Do not provide API secrets until they are excluded from profile fields and protected credential storage has been verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [API interface reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON assessment; Markdown for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual moisture indicators, risk level, suggested husbandry checks, and a report link. The assessment is not a veterinary diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
