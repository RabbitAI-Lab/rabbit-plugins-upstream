## Description:

Analyzes pet oral images or videos to describe visible gum color and tartar coverage and provide non-diagnostic oral health observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers of pet cameras or health platforms can submit oral images or videos for visible gum and tartar observations, review suggested follow-up, and retrieve prior reports. Results are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet oral images, videos, or URL references are sent to a cloud service.

Mitigation: Submit media only when cloud processing is acceptable and avoid including unnecessary sensitive content.

Risk: The skill may create or reuse an internal identity and store service tokens in its local workspace.

Mitigation: Use an isolated workspace and account, and protect local data as credential-bearing.

Risk: History lookup can retrieve cloud-stored reports under that identity.

Mitigation: Request history only when you intend to access prior reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-oral-snapshot-gum-redness-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown with structured analysis results and report links; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a local file or list cloud-stored report history.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; bundled frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
