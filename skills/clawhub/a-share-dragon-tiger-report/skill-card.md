## Description:

Generates structured Chinese-language A-share limit-up and Dragon-Tiger List research reports with layered screening, quantitative analysis, and risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and investors use the skill to organize A-share trading-day data into limit-up and Dragon-Tiger List research reports, screening notes, and risk checks. It is intended for research and education; its outputs are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial reports may contain misleading conclusions or data, and the security review notes that report-writing purpose and some behaviors do not fully align.

Mitigation: Verify data dates, sources, and calculations independently; treat report conclusions as research material rather than trade instructions.

Risk: The security review identifies a browser-side injection risk.

Mitigation: Inspect and sanitize generated HTML before opening it, especially when it contains externally supplied content; use an isolated browser profile for review.

Risk: The artifact includes GitHub publishing instructions that could publish files to an unintended remote if followed without review.

Mitigation: Review the files and confirm the repository remote and target branch before running publishing commands.

Risk: The artifact documents reinstall behavior using rsync --delete, which can remove files from the destination directory.

Mitigation: Confirm the destination path and back up its contents before running the sync command.

Risk: Security scanner coverage was partial, so uninspected portions are not established as safe.

Mitigation: Review the complete artifact and its behavior before installation; do not treat the absence of listed findings as a clean result.

## Reference(s):

- [Project homepage](https://github.com/yjkj999999/a-share-dragon-tiger-strategy)
- [Anthropic S-1 filing referenced for A-share AI-chain mapping](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, PDF, JSON]

**Output Format:** [Chinese-language research reports, exported as HTML and PDF, with supporting JSON data; PPTX is available in the optional classic style.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily report generation is limited to trading days. If live data is unavailable, local sample data is labeled as demonstration data; report conclusions are not investment advice.]

## Skill Version(s):

4.0.2 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
