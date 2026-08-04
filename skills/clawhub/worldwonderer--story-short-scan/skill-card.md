## Description: <br>
Analyzes short-form Chinese web fiction rankings across platforms such as Zhihu Yanyan, Qimao, Heiyan, and Dianzhong to identify current genre, emotion, and topic trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and market analysts use this skill to scan short-form web fiction rankings, compare platform patterns, and turn sampled market signals into topic candidates, risk thresholds, and follow-up validation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Heiyan collection path can use a logged-in Chrome admin session to access backend management APIs, and generated reports may contain non-public book metadata. <br>
Mitigation: Run the skill only with an account that has the minimum necessary access, prefer public or platform-approved exports where possible, and review generated reports before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-scan) <br>
- [OpenClaw metadata link](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Short-form web fiction market data reference](references/real-market-data.md) <br>
- [Dianzhong browse page](https://www.ishugui.com/browse) <br>
- [Heiyan booklist page](https://manage.zhangwenpindu.cn/books/booklist) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports with tables, optional JavaScript scraper commands, and generated market-scan data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should include sample date, trend confidence, and rescan timing; browser-CDP collection may require an authenticated browser session.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
