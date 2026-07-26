## Description: <br>
Helps agents fetch, present, and optionally export ranked WeChat Official Account original article recommendations from RedFox data by category and date range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use when a user wants recent or historical rankings of original viral WeChat articles, category-filtered article discovery, HTML/PDF-style ranking reports, or daily niche subscription prompts based on RedFox article data. <br>

### Deployment Geography for Use: <br>
Global, subject to the availability and terms of RedFox and WeChat-linked services. <br>

## Known Risks and Mitigations: <br>
Risk: The API script disables TLS certificate verification while sending the RedFox API key and query metadata. <br>
Mitigation: Use only after trusting RedFox, avoid sensitive query metadata, keep the API key scoped and revocable, and fix TLS verification before normal use. <br>
Risk: Generated HTML is built from remote article data and links. <br>
Mitigation: Treat generated HTML as untrusted output, review it before sharing or opening in privileged contexts, and avoid exposing secrets in generated files. <br>
Risk: The security verdict is suspicious and subscription behavior is not fully clarified. <br>
Mitigation: Review the skill before deployment and avoid vague requests or subscription flows until the expected behavior is confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-original-hot) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFoxHub](https://redfox.hk?source=github) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, html] <br>
**Output Format:** [Markdown article tables and status text, with optional generated HTML ranking pages suitable for PDF export.] <br>
**Output Parameters:** [Category, date range, result limit, RedFox API key, source name, temporary article data file, output HTML path, and display count.] <br>
**Other Properties Related to Output:** [Outputs are based on remote RedFox API data and may include WeChat article links, account links, read counts, data freshness notes, and subscription prompts.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
