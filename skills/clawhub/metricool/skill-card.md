## Description: <br>
Schedule and manage social media posts via Metricool API across LinkedIn, X, Bluesky, Threads, Instagram, and Facebook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[willscott-v2](https://clawhub.ai/user/willscott-v2) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Social media operators and developers use this skill to list Metricool brands, schedule multi-platform posts, review queued posts, and check suggested posting times from the Metricool API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can schedule public social posts using stored Metricool credentials. <br>
Mitigation: Review the exact text, platforms, scheduled time, timezone, and account before running schedule-post.js. <br>
Risk: The skill may use the first connected Metricool brand when a brand ID is not provided. <br>
Mitigation: Run get-brands.js first and pass an explicit blogId for scheduling and account-specific queries. <br>
Risk: Metricool tokens can grant authority over connected social accounts if exposed. <br>
Mitigation: Prefer environment-injected credentials or a dedicated Metricool-only config, and keep tokens out of committed .env files. <br>


## Reference(s): <br>
- [Metricool](https://metricool.com) <br>
- [Metricool Skill on ClawHub](https://clawhub.ai/willscott-v2/skills/metricool) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request examples; scripts can print plain text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Metricool user credentials; scheduling commands can create public social posts on connected accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
