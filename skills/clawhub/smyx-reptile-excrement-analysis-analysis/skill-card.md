## Description:

Through a fixed camera in the reptile enclosure, the system captures a high-definition image or static video frame after excrement is found, then uses AI visual analysis to identify urate size and feces morphology.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze reptile enclosure images or video frames for urate color, urate area, feces color, feces consistency, species-specific context, and alert-level guidance. It is intended for visual assessment and care prompts, not veterinary diagnosis or medication instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure images, videos, report history, and account identifiers may be sent to a remote service.

Mitigation: Require user confirmation before uploads or history queries, and review retention, deletion, and account-linking behavior before deployment.

Risk: Network configuration and endpoint handling are under-scoped for production use.

Mitigation: Approve only production HTTPS endpoints, document token storage, and restrict accepted input URLs before installation.

Risk: Visual health assessments may be mistaken for veterinary diagnosis.

Mitigation: Keep outputs limited to visual findings and care prompts, avoid medication or procedure instructions, and direct users to a qualified reptile veterinarian for abnormal results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis)
- [Reptile Excrement Analysis API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown-style status text with structured JSON analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a file when requested by the caller.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
