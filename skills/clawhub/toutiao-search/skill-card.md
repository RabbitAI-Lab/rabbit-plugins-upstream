## Description: <br>
今日头条爆款内容查询 — 输入关键词搜索今日头条最新作品（图文/视频），支持按阅读量/时间排序、限定时间范围，终端表格展示 + CSV 导出 + 交互式 HTML 报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content analysts use this skill to search recent Toutiao articles and videos, track hot topics, monitor competitor or brand keywords, and export results for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports can expose the user's Redfox API key. <br>
Mitigation: Use a low-privilege Redfox API key, avoid sharing generated HTML reports, and prefer CSV-only mode when an interactive report is not required. <br>
Risk: The local report proxy is unauthenticated while the report server is running. <br>
Mitigation: Run the report server only on a trusted machine, keep it bound to localhost, stop it when finished, and prefer a revised version with proxy protection for shared environments. <br>
Risk: Search terms are sent to Redfox services. <br>
Mitigation: Avoid sensitive search terms unless the user is comfortable sending those queries to Redfox. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/toutiao-search) <br>
- [Redfox API key settings](https://redfox.hk/settings/api-keys?source=redskill) <br>
- [Redfox Toutiao searchWork API](https://redfox.hk/story/api/toutiao/searchWork) <br>
- [Redfox Toutiao workDetail API](https://redfox.hk/story/api/toutiao/workDetail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Terminal text plus CSV files and interactive HTML reports; usage guidance is Markdown with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Redfox API key. By default the script writes CSV and HTML reports under ~/Downloads/QoderToutiaoSearch and may start a local browser report server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
