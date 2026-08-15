## Description:

eKYC Suite Media Labeling is a focused KYC media-labeling and KYC image-labeling skill that returns structured label results from a configured eKYC Suite Cloud backend for consented images or videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carochen112233-commits](https://clawhub.ai/user/carochen112233-commits)

### License/Terms of Use:

MIT-0

## Use Case:

External KYC onboarding, fraud review, identity operations, and human-review teams use this skill to request supported portrait, behavior, and scene labels from authorized media. The labels should support review and triage workflows, not final high-impact decisions without human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive KYC media to a configured cloud backend.

Mitigation: Install only for authorized KYC or eKYC media review, use a trusted HTTPS endpoint, and confirm retention, access, and review policies before processing media.

Risk: Liveness or comparison processing may be enabled even when the intended workflow is narrow media labeling.

Mitigation: Verify what the backend does with doLive and doCompare, and set those flags to 0 unless that processing is explicitly intended and permitted.

Risk: Structured media labels can be misused as definitive facts or final eligibility decisions.

Mitigation: Treat labels as review signals, escalate sensitive or ambiguous results to authorized reviewers, and avoid unsupported inferences about protected traits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-media-labeling)
- [Related npm MCP package](https://www.npmjs.com/package/@wefi-ai/ekyc-suite-media-labeling-mcp)
- [Parent eKYC Suite skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite)
- [eKYC Suite Face Compare skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-face-compare)
- [eKYC Suite AI Guardian skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-ai-guardian)
- [eKYC Suite Document OCR skill](https://clawhub.ai/carochen112233-commits/skills/ekyc-suite-document-ocr)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration, Guidance]

**Output Format:** [JSON label results plus concise Markdown command and handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one image or video input and 1-5 supported label codes; the configured backend may also process liveness or comparison flags when explicitly enabled.]

## Skill Version(s):

1.0.16 (source: SKILL.md frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
