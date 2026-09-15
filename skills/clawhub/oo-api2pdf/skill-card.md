## Description:

API2PDF (api2pdf.com). Use this skill for ANY API2PDF request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert Markdown content into PDFs through API2PDF with an OOMOL-connected account and the oo CLI. It is suited for workflows that need generated PDF URLs and conversion metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Markdown converted through this workflow is sent to OOMOL/API2PDF as an external content-generation action.

Mitigation: Install and use the skill only for content that is appropriate to share with OOMOL/API2PDF, and treat generated PDFs as outputs from an external service.

Risk: The skill guidance includes one-line remote installer commands, which the security evidence flags as unsafe to run blindly.

Mitigation: Use a verified or package-manager installation path where possible, and review installer commands before execution.

Risk: The security evidence notes that PDF generation is under-labeled as read-like even though it creates external generated output.

Mitigation: Review the exact Markdown payload and expected PDF-generation effect before running conversion actions.

## Reference(s):

- [ClawHub API2PDF Skill](https://clawhub.ai/oomol/skills/oo-api2pdf)
- [API2PDF Homepage](https://www.api2pdf.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce API2PDF-generated PDF URLs and conversion metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
