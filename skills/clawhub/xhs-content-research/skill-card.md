## Description: <br>
用于小红书内容研究、热门笔记样本、内容角度、关键词调研、选题参考、竞品内容观察和趋势素材整理。覆盖 Xiaohongshu / XHS / RedNote note research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, researchers, and content strategists use this skill to research public Xiaohongshu / XHS / RedNote notes for keyword research, topic ideas, competitor content observation, trend material, sample tables, content angles, and engagement signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the SocialDataX npm package and API service. <br>
Mitigation: Install and use it only after confirming you trust the package, the API service, and the account tied to SOCIALDATAX_API_KEY. <br>
Risk: Outputs may include full Xiaohongshu note URLs with xsec_token query parameters. <br>
Mitigation: Review destinations before displaying, storing, or forwarding returned URLs, especially outside the user's intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research) <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown research report with sample tables, concise analysis, URLs, note IDs, and optional shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node and npm when using the direct CLI.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
