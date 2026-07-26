## Description: <br>
Linkfox Amazon Ads helps agents authorize Amazon Ads accounts, manage SP/SB/SD ads, and retrieve Amazon Ads reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce advertisers, operators, and developers use this skill to bind Amazon Ads accounts, inspect or update ad entities, and pull structured campaign performance reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Amazon Ads credentials and business reports. <br>
Mitigation: Install and run it only in an environment approved for local storage of those credentials and reports, and review generated outputs before sharing them. <br>
Risk: API host and credential behavior depends on environment configuration. <br>
Mitigation: Use trusted environment variables for API keys and host configuration, and avoid untrusted runtime configuration. <br>
Risk: Report-serving features and persisted outputs may expose advertising data if used carelessly. <br>
Mitigation: Keep report-serving local, avoid binding it to non-local interfaces, and clean persisted outputs when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads) <br>
- [Amazon Ads authorization reference](artifact/references/linkfox-amazon-ads-auth.md) <br>
- [Amazon Ads management reference](artifact/references/linkfox-amazon-ads-manager.md) <br>
- [Amazon Ads reporting reference](artifact/references/linkfox-amazon-ads-report.md) <br>
- [Sponsored Products API reference](artifact/references/api/sp.md) <br>
- [Sponsored Brands API reference](artifact/references/api/sb.md) <br>
- [Sponsored Display API reference](artifact/references/api/sd.md) <br>
- [Report types index](artifact/references/report-types/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Files] <br>
**Output Format:** [Markdown guidance with command examples, JSON API responses, and generated report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local JSON responses and downloaded report data; report-serving links are time-limited.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
