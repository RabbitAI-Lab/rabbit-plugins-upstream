## Description:

OpenClaw Web Clipper saves user-provided web pages as clean local Markdown with YAML frontmatter, using multiple extraction engines with batch clipping and duplicate detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to ask an agent to fetch selected web pages, extract article content, and save local Markdown clippings that can later be indexed by a knowledge-base workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested web pages may contain private, paywalled, or sensitive content that becomes searchable after it is saved locally.

Mitigation: Clip only URLs the user intentionally provides, keep output in a dedicated clippings folder, and avoid clipping content that should not be stored in a local knowledge base.

Risk: Batch URL lists may save more pages than intended.

Mitigation: Review batch files before running them and inspect the generated files and .clips-index.json after completion.

Risk: Extraction can fail or produce incomplete text on pages with anti-bot controls or unusual page structure.

Mitigation: Review generated Markdown before relying on it; the skill reports blocked pages such as 403 or 521 responses and does not bypass site restrictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-web-clipper)
- [Project documentation](https://github.com/dtsola/xiaoyaoclaw-web-clipper)
- [Design document](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown files with YAML frontmatter, terminal status messages, and optional shell commands for clipping or indexing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes .md clipping files and a .clips-index.json deduplication index in the configured output directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
