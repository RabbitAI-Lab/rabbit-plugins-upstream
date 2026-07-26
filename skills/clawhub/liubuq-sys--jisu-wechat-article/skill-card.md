## Description: <br>
Searches WeChat public account articles by keyword and returns article titles, summaries, publish times, source accounts, and links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liubuq-sys](https://clawhub.ai/user/liubuq-sys) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to search WeChat public account articles, collect structured article metadata, optionally resolve real WeChat article links, and export results for downstream review or planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs web scraping and optional redirect resolution or article content fetching against Sogou and WeChat pages. <br>
Mitigation: Use those options deliberately, respect Sogou and WeChat terms and rate limits, and expect site controls to block some content fetches. <br>
Risk: The optional JSON output path can create or overwrite a result file. <br>
Mitigation: Provide an output path only in a location where writing or overwriting a JSON result file is acceptable. <br>
Risk: High-frequency use may trigger anti-spider controls or account/network blocking. <br>
Mitigation: Limit request volume, use configured retry and delay options conservatively, and run in a restricted network environment when stronger boundaries are needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/liubuq-sys/skills/jisu-wechat-article) <br>
- [Sogou Weixin Search](https://weixin.sogou.com/weixin) <br>
- [wechat-mp Companion Skill](https://clawhub.ai/jisuapi/wechat-mp) <br>
- [JisuAPI](https://www.jisuapi.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown instructions and structured search results, with optional JSON output from the Python script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include title, summary, publish time, source account, link fields, and optional resolved-link or fetched-content status fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
