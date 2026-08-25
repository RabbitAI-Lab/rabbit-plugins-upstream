## Description:

ct-advisor is a clinical-trial lifecycle advisor that answers methodology, design, regulatory, compliance, quality, safety, document, and tone questions, and routes registry, literature, safety, and sample-size needs to related ct-series skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, and medical students use this skill in chat to get clinical-development guidance, regulatory and methodology advice, document and QC support, and routed outputs from related ct-series data and computation skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical-trial questions may be sent to an author-hosted Coze service with a stable device hash.

Mitigation: Do not enter patient identifiers, unpublished sponsor data, trade secrets, passwords, API keys, or other restricted information; review the outbound behavior before installation.

Risk: Local memory or context-cache behavior may conflict with strict session-only handling requirements.

Mitigation: Review or disable local memory and context-cache behavior when strict session-only processing is required.

Risk: Optional bug reports are outbound submissions.

Mitigation: Send bug reports only after checking the preview and removing sensitive or confidential information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project homepage](https://github.com/medstatstar/ct-advisor)
- [English README](https://github.com/medstatstar/ct-advisor/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/ct-advisor/blob/main/README_zh-CN.md)
- [Original clinical-trial-advisor project](https://github.com/A-xin946/clinical-trial-advisor)
- [Workflow steps](references/steps.md)
- [Reference index](knowledge/reference-index.md)
- [Search sites reference](references/search-sites.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text chat responses, sometimes with command snippets, configuration guidance, or stitched outputs from sibling ct-series skills.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single conversational response; may include routed clinical-trial data, literature, safety, or sample-size outputs when sibling skills are available.]

## Skill Version(s):

0.9.100 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
