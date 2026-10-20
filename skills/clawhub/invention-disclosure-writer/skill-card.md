## Description:

Creates invention-disclosure documents and patent-direction analyses from R&D materials or early-stage technical ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External inventors, developers, and R&D teams use this skill to turn technical materials or an early-stage idea into an invention disclosure, patent-point analysis, and review notes. Users should verify the technical content and review confidentiality and charges before submitting materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that users are asked to share live API keys in chat and that saved keys have no specified access protections.

Mitigation: Configure PATENTMAX_API_KEY outside chat, retain the default HTTPS endpoint, and use credential-safe redirect handling.

Risk: Technical disclosures may contain confidential information and are retained for the lifetime of the PatentMax account, according to the cited privacy policy.

Mitigation: Upload only selected materials the user is authorized to share, and review PatentMax's privacy policy before uploading.

Risk: Submitting a report may incur a charge.

Mitigation: Review and approve each charge before submission.

## Reference(s):

- [Workflow](references/workflow.md)
- [Materials Guide](references/materials-guide.md)
- [FAQ](references/faq.md)
- [PatentMax API Platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Files, Text, Analysis, Guidance]

**Output Format:** [Word (.docx) invention disclosure and review notes, with JSON result data and user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated patent analyses are proposals that require review. Submission may incur charges.]

## Skill Version(s):

1.1.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
