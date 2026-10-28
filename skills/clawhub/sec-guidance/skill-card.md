## Description:

Extract management guidance and forward-looking statements from SEC filings with verifiable inline citations and a retrieval recall check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tinghao0724](https://clawhub.ai/user/tinghao0724)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and financial researchers use this skill to review management outlook and forward-looking statements in SEC filings, then verify claims against cited source passages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud synthesis may send the question and filing excerpts to an external AI provider and may incur charges.

Mitigation: Unset both provider API keys for retrieval without cloud synthesis, or use the offline demo.

Risk: Filing selection or retrieval may omit relevant guidance or surface passages that do not support a claim.

Mitigation: Choose an explicit filing form when it matters, verify citations against the filing, and review the recall check.

Risk: Dependencies and optional heavy-mode integrations introduce environment and trust considerations.

Mitigation: Install dependencies in an isolated environment and configure heavy mode only with a trusted local pipeline.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/tinghao0724/skills/sec-guidance)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Plain text or JSON with inline citations, source quotations, and filing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a retrieval recall check that identifies guidance-dense passages not surfaced in the results.]

## Skill Version(s):

0.4.3 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
