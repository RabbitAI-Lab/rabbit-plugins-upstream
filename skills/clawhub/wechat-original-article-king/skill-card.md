## Description: <br>
全网持续收录每日公众号原创热门文章内容，向用户推送公众号原创热门文章；当用户需要获取全领域的公众号原创热门文章、或订阅每日原创热门文章推送时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External WeChat editors, content planners, content creators, and operations teams use this skill to retrieve original WeChat article rankings by category or date, inspect current content trends, and generate shareable HTML/PDF-ready reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends REDFOX_API_KEY to the RedFox service and the evidence flags the release for review. <br>
Mitigation: Install only if the RedFox service is trusted, confirm the key scope and revocation process, and keep the key out of code, prompts, logs, and generated files. <br>
Risk: The evidence reports deliberately unverified HTTPS in the API client. <br>
Mitigation: Remove the TLS verification bypass before use and require normal certificate and hostname validation. <br>
Risk: Generated HTML reports load third-party CDN JavaScript. <br>
Mitigation: Avoid external CDN dependencies in generated reports or clearly disclose them before opening or sharing the report. <br>
Risk: Subscription behavior is described in the skill but not fully specified by the included code. <br>
Mitigation: Review and define subscription handling, storage, consent, and cancellation behavior before enabling recurring pushes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-original-article-king) <br>
- [README.en.md](README.en.md) <br>
- [README.md](README.md) <br>
- [Category mapping](references/category_mapping.md) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox service](https://redfox.hk) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown tables and generated HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY. Article data is a fetch-time snapshot, follows the service update schedule, and is documented with a 30-day lookback.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
