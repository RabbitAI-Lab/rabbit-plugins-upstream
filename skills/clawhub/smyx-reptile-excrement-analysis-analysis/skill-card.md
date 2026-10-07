## Description:

Analyzes reptile enclosure images for urate size and feces appearance, then provides an assessment and alerts based on the observed waste.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and developers of enclosure-monitoring tools use this skill to review images of reptile waste, track urate and feces changes, and retrieve assessment reports. Its health prompts are observational, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure images or URLs are sent to an external analysis service.

Mitigation: Use only with appropriate consent and after checking the service's data-handling terms; avoid submitting sensitive or unnecessary imagery.

Risk: The skill silently creates or reuses an account-linked identity and persists identifiers or tokens locally.

Mitigation: Review or clear the workspace data directory and smyx-api-key.txt when persistent identity or credential reuse is unwanted.

Risk: Image-based health prompts may be mistaken for a veterinary diagnosis.

Mitigation: Treat assessments as screening guidance, and consult a reptile veterinarian for concerning or persistent findings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis)
- [Reptile excrement analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured assessment or Markdown report list; optional JSON and saved report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes urate and feces observations, alerts, suggested follow-up, and report links when available.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata; bundled skill frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
