## Description: <br>
Analyzes short-form web fiction rankings across Zhihu Yanyan, Qimao, Heiyan, and Dianzhong to identify current emotional hooks, topic trends, risks, and validation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and market analysts use this skill to scan short-form web fiction platforms, compare current ranking samples, and turn those signals into story direction candidates and follow-up validation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reuse a logged-in browser session and read an admin cookie to access private Heiyan management data. <br>
Mitigation: Use it only with authorized access, prefer public-page collection or a dedicated least-privilege account, and treat generated Markdown files as potentially private business or catalog data. <br>
Risk: Short-form fiction trend conclusions can become stale quickly or rely on historical reference data when live collection is unavailable. <br>
Mitigation: Label sample dates and confidence, rescan before treating a topic as current, and keep unverified historical patterns as candidate hypotheses. <br>


## Reference(s): <br>
- [Short Web Fiction Market Reference](references/real-market-data.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-short-scan) <br>
- [OpenClaw Metadata Source](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Dianzhong Male Short Fiction Browse](https://www.ishugui.com/browse) <br>
- [Dianzhong Female Short Fiction Browse](https://www.ishugui.com/browse/on3) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with tables and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce dated Markdown data files when browser-based collection scripts are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
