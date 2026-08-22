## Description:

用于搜索免费官方年报、年度报告、定期报告、上市公司披露文件、债券发行人报告和海外公司年度账目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and agents use this skill to find free official annual reports, periodic filings, issuer reports, and related disclosure pages across supported public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled downloader can fetch any URL and overwrite a user-specified local file path.

Mitigation: Use only trusted official report URLs and constrain downloads to a dedicated reports directory with reviewed output paths.

Risk: The security verdict is suspicious because broad filesystem or network access increases impact if the skill is misused.

Mitigation: Review the skill before installation and run it with limited filesystem and network permissions where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-year-report)
- [CNINFO disclosure search](https://www.cninfo.com.cn/new/index?lang=zh)
- [SSE periodic reports](https://www.sse.com.cn/disclosure/listedinfo/regular/)
- [SZSE company announcements](https://www.szse.cn/www/disclosure/notice/company/)
- [HKEXnews predefined documents](https://www1.hkexnews.hk/search/predefineddoc.xhtml)
- [SEC EDGAR submissions API](https://data.sec.gov/submissions/)
- [Companies House company search](https://find-and-update.company-information.service.gov.uk/)
- [SEDAR+ document search](https://www.sedarplus.ca/csa-party/service/create.html?_locale=en&service=searchDocuments&targetAppCode=csa-party)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files, Markdown]

**Output Format:** [Markdown guidance with optional JSON API responses and downloaded report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve company or security code, report period, title, disclosure date, source, and PDF or official detail-page URL.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
