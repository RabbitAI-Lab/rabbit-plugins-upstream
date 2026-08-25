## Description:

青虎AI Shopee 跨站点拓客 helps sellers compare brand and category distribution, trends, shops, and product activity across Shopee sites to decide which site to open next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, marketplace operators, and analysts use this skill to evaluate cross-site expansion opportunities. It supports brand-led and category-led site prioritization using Qinghu data, then returns concise recommendations, comparison tables, localization notes, and reasons to avoid unsuitable sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a Qinghu API token for confirmed calls that can consume account credits.

Mitigation: Confirm intended Qinghu calls before use, keep the token in approved secret storage or environment variables, and review reported point costs from the response envelope.

Risk: Returned market datasets may be exported or cached as local spreadsheet files.

Mitigation: Store exported files only in approved workspaces and avoid exposing cached datasets or file paths to users or tools that should not access them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-cross-site)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown recommendations with optional spreadsheet exports and inline JSON or shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce site priority rankings, comparison tables, localization notes, risk notes, API call examples, and local spreadsheet files for larger returned datasets.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
