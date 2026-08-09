## Description:

YuanDian Law and Case Search helps agents query Chinese statutes, regulations, cases, and company records, then archive results and generate traceable legal research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Legal professionals and researchers use this skill to retrieve Chinese legal authorities, compare related cases, check cited law or cases, and prepare research reports with archived source material. It is also documented for authorized company due diligence workflows.

### Deployment Geography for Use:

Global; the data source and legal coverage focus on Chinese law and YuanDian/open.chineselaw.com.

## Known Risks and Mitigations:

Risk: Legal queries, case facts, company identifiers, and hallucination-check text may be sent to YuanDian/open.chineselaw.com.

Mitigation: Use the skill only for appropriate matters, minimize or redact sensitive content before submission, and review the platform terms for retention and handling.

Risk: The skill stores legal and business research results locally by default, including archive files and Markdown report copies that may contain sensitive information.

Mitigation: Use --no-cwd-report or --no-report for confidential matters, keep archive outputs out of shared folders and version control, and review generated files before sharing.

Risk: The documentation suggests a broad danger-full-access/no-approval Codex setup for network-constrained environments.

Mitigation: Avoid that setup unless the workspace is isolated and the data is suitable for local script execution; prefer least-privilege execution where possible.

Risk: The skill reads API credentials from scripts/.env or YD_API_KEY.

Mitigation: Keep credentials out of shared folders and repositories, restrict file access, and rotate the API key if exposure is suspected.

Risk: Enterprise profiling can involve business-sensitive due diligence data.

Mitigation: Use enterprise endpoints only for separately authorized due-diligence tasks and disclose source limitations in downstream reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/yuandian-law-search)
- [Publisher profile](https://clawhub.ai/user/cat-xierluo)
- [YuanDian Open Platform](https://open.chineselaw.com)
- [Clawdis homepage metadata](https://github.com/cat-xierluo/legal-skills)
- [Research middleware](references/07-research-middleware.md)
- [Typical workflows](references/02-typical-workflows.md)
- [Report consolidation](references/03-report-consolidation.md)
- [API endpoint manifest](endpoints/MANIFEST.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, text summaries, shell command invocations, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write archived JSON and Markdown research artifacts locally unless report writing is disabled.]

## Skill Version(s):

1.8.8 (source: server release, frontmatter, and changelog; released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
