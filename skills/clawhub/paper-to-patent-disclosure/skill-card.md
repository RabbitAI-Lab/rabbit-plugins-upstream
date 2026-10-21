## Description:

Helps users turn their own papers or research results into a patent technical disclosure by identifying patentable points and publication risks before drafting a Word document for selected points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers and inventors use the skill to assess publication risks and identify candidate patentable points in their own research, then prepare a technical disclosure for selected points. It does not process papers attributed to others.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid-account API key may be exposed if credential forwarding follows an insecure or cross-origin redirect.

Mitigation: Before using a paid-account key, require HTTPS and reject insecure or cross-origin redirects.

Risk: Unpublished research text may be uploaded to PatentMax without the user having confirmed confidentiality and retention terms.

Mitigation: Confirm which paper content will be uploaded and review the service's confidentiality and retention terms before submission.

Risk: Locally saved credentials or paid generation requests may be used without adequate user oversight.

Mitigation: Protect saved credentials, prefer a limited trial key, and obtain approval for each paid generation.

## Reference(s):

- [Complete workflow](references/workflow.md)
- [Preparing source materials](references/materials-guide.md)
- [Frequently asked questions](references/faq.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [ClawHub release](https://clawhub.ai/ip930/skills/paper-to-patent-disclosure)

## Skill Output:

**Output Type(s):** [Analysis, Text, Word document, JSON]

**Output Format:** [Patent-point and publication-risk analysis in text; technical disclosure and review notes in .docx; structured result in JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user selects which candidate points to draft; the disclosure is accompanied by notes identifying inferred or missing details.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
