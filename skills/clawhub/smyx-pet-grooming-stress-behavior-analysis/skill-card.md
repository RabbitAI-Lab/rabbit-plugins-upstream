## Description:

Analyzes pet grooming videos or video URLs through a server-side API to identify stress behaviors such as struggling, panting, and tail tucking, then returns stress grading and a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet grooming session media for observable stress behaviors and retrieve structured reports or cloud history for grooming shops, veterinary clinics, and pet care services. Results are for behavior observation support, not disease diagnosis or behavior correction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet grooming media or video URLs may be sent to the configured backend for analysis.

Mitigation: Review endpoint configuration and obtain appropriate consent before using the skill with pet grooming media.

Risk: The skill can create or reuse an internal identity, query cloud history for that identity, and store account tokens in the workspace.

Mitigation: Require explicit consent for history lookup and identity or account creation, and review local token storage before installation.

Risk: Development or debug endpoint settings could route analysis to unintended services.

Mitigation: Disable dev and debug settings and verify production endpoint configuration before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Interface Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; local video inputs are limited to supported formats and size limits documented by the artifact.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
