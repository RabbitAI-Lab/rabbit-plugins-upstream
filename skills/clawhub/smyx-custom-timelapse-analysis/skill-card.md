## Description:

Generates condensed album highlights based on specified keywords or targets, extracting target segments from long videos and compiling them into a summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local or URL-based video inputs, request keyword or target-based clip extraction, and receive structured time-lapse highlight analysis or historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media may be uploaded to cloud services for analysis.

Mitigation: Use only footage approved for cloud processing, and avoid sensitive or regulated media unless the deployment owner accepts that data flow.

Risk: The skill silently creates or reuses an account identity and may store account-linked tokens locally.

Mitigation: Review local data storage and account-linking behavior before installation, and clear stored identity data when retiring the skill.

Risk: Historical report retrieval is cloud-backed and account-linked.

Mitigation: Treat report listings and links as account data, and restrict use to environments where cloud history access is expected.

Risk: The custom target or keyword option should not be trusted to limit what the backend analyzes.

Mitigation: Do not rely on the text target as a privacy boundary; assume the submitted media can be processed broadly by the backend service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON text with structured analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; can save output to a caller-provided file path.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
