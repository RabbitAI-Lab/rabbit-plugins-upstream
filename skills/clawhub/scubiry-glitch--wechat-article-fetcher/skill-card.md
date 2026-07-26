## Description: <br>
Fetches WeChat public account article content and extracts structured summaries when users provide mp.weixin.qq.com links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scubiry-glitch](https://clawhub.ai/user/scubiry-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to recover, summarize, analyze, and optionally archive WeChat public account articles from mp.weixin.qq.com links when direct page fetching is unreliable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Archived article content may include private, internal, or copyrighted material. <br>
Mitigation: Confirm user intent and access rights before saving full text to Feishu or local Markdown, and avoid republishing full copyrighted content. <br>
Risk: WeChat anti-scraping and JavaScript rendering can make automated fetching incomplete or unreliable. <br>
Mitigation: Ask the user for screenshots, pasted text, or exported content when direct fetching fails; label summaries based on partial content accordingly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/scubiry-glitch/skills/wechat-article-fetcher) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text summaries and extraction guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured article fields such as title, author, date, key points, summary, and archive notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
