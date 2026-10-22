## Description:

Analyze the structure, layout, and content of PDF documents using MinerU, returning structured output that preserves headings, tables, images, formulas, and document hierarchy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mzlzyca](https://clawhub.ai/user/mzlzyca)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, researchers, and document-processing teams use this skill to inspect PDFs, extract structured document content, and preserve layout details such as headings, tables, images, formulas, and page ranges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDFs selected for analysis may be processed by the MinerU service.

Mitigation: Do not process confidential, regulated, or internal documents unless external API processing is allowed by policy.

Risk: Installing the MinerU CLI globally or from a moving latest version can increase supply-chain and privilege risk.

Mitigation: Prefer a pinned CLI version and avoid running global installs with elevated privileges.

Risk: Full extraction requires a MinerU token.

Mitigation: Store MINERU_TOKEN as an environment variable or through the CLI auth flow and avoid exposing it in shared logs or files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mzlzyca/skills/pdf-analysis)
- [ClawHub Publisher Profile](https://clawhub.ai/user/mzlzyca)
- [MinerU Homepage](https://mineru.net)
- [MinerU Token Management](https://mineru.net/apiManage/token)
- [MinerU Source Repository](https://github.com/opendatalab/MinerU)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured document outputs from MinerU, with setup and execution commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quick extraction writes Markdown to stdout by default or to a selected output directory; full extraction can produce richer formats and requires a MinerU token.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
