## Description:

Selling Point analyzes ARI-collected Amazon review data to identify purchase drivers, recurring positive themes, pain points, trends, competitor differences, and listing copy opportunities for Amazon ASINs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and agencies use this skill to turn ARI review data for ASINs into selling-point prioritization, VOC summaries, trend checks, and listing improvement suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some ARI flows can spend account credits without a fresh per-operation confirmation when account rules allow auto-confirmation.

Mitigation: Before first use, tell the agent "only quote, do not execute" or "ask me before every credit charge" when you want explicit approval for paid actions.

Risk: Exports can overwrite local files if run from a broad output directory.

Mitigation: Run export commands from a dedicated empty folder or set ARI_EXPORT_DIR to a narrow export directory before exporting reports or review CSV files.

Risk: The skill requires trusting ARI with an API key and account-level actions.

Mitigation: Use the documented browser authorization flow, do not paste API keys into chat, and install only if ARI is an acceptable third-party service for the user's Amazon review workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/selling-point)
- [README](README.md)
- [Usage guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API key management](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text responses, with occasional JSON or shell command snippets for setup, quotations, reports, exports, or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, CSV/Markdown/HTML export paths, sample-scope notes, and credit usage or quotation details returned by ARI.]

## Skill Version(s):

1.4.11 (source: server release evidence, artifact frontmatter, _meta.json, CHANGELOG, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
