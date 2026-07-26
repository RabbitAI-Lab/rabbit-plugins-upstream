## Description: <br>
Fetches Amazon Ads reports for Sponsored Products, Sponsored Brands, and Sponsored Display by creating, polling, downloading, and returning structured report data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and e-commerce operators use this skill to retrieve Amazon Ads performance reports across SP, SB, and SD report types. It helps select report definitions, run the reporting workflow, and return structured data for campaign, keyword, search term, product, and related advertising analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon Ads reports, saved report paths, and temporary local download links can contain sensitive business data and may be retained locally after use. <br>
Mitigation: Install only in a trusted local environment, prefer disabling local HTTP serving for sensitive reports, keep serving bound to 127.0.0.1, and delete generated report files when they are no longer needed. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-report) <br>
- [API and runtime parameter reference](references/api.md) <br>
- [Amazon Ads report type index](references/report-types/index.md) <br>
- [Sponsored Products report types](references/report-types/sp/) <br>
- [Sponsored Brands report types](references/report-types/sb/) <br>
- [Sponsored Display report types](references/report-types/sd/) <br>
- [Amazon Ads Reporting v3 report types](https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON responses, saved report files, local file links, and concise text summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large responses are saved under the current working directory; temporary local HTTP links may be served unless disabled.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
