## Description: <br>
全网持续收录每日超过1000+公众号10w+文章内容，向用户推送公众号达到10w+阅读的热门文章；当用户需要获取全领域的公众号热门文章、或订阅每日10w+文章推送、特定领域爆款文章时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content teams, WeChat account operators, editors, marketers, and growth researchers use this skill to retrieve RedFox-ranked WeChat 10w+ article lists by category and date, analyze viral patterns, subscribe to updates, and export HTML/PDF reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a RedFox API key and sends article queries to redfox.hk. <br>
Mitigation: Provide REDFOX_API_KEY through a managed environment or secret setting, confirm key scope and revocation options, and avoid exposing the key in prompts, logs, code, or output files. <br>
Risk: A referenced API spec describes reading shell profile files for an API key, which is broader credential access than this skill needs. <br>
Mitigation: Do not allow the agent to search shell profile files for credentials; supply REDFOX_API_KEY explicitly through the runtime environment. <br>
Risk: Generated JSON and HTML reports are stored on disk and may contain article metadata or working context. <br>
Mitigation: Store generated files in an approved workspace, review contents before sharing, and remove temporary files when they are no longer needed. <br>
Risk: Exported HTML reports load html2pdf.js from a third-party CDN when opened for PDF export. <br>
Mitigation: Open generated HTML only in environments where loading that CDN is acceptable, or replace the CDN dependency with an approved local copy before export. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-10w-hot) <br>
- [API interface specification](references/api-spec.md) <br>
- [Category mapping reference](references/category-mapping.md) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox WeChat article API endpoint](https://redfox.hk/story/api/cozeSkill/getWxDataByCategoryAndTime) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Files, Configuration guidance] <br>
**Output Format:** [Markdown article rankings and analysis, shell command examples, JSON temp data, and generated HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; generated HTML reports load a third-party CDN script for PDF export.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
