## Description: <br>
用于小红书内容研究、热门笔记样本、内容角度、关键词调研、选题参考、竞品内容观察和趋势素材整理。覆盖 Xiaohongshu / XHS / RedNote note research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketers, and content researchers use this skill to research public Xiaohongshu/XHS/RedNote notes for content angles, keyword research, competitor observation, trend material, and topic inspiration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to SocialDataX with the user's SOCIALDATAX_API_KEY. <br>
Mitigation: Use only queries appropriate to share with SocialDataX and configure the API key in the runtime environment rather than embedding it in files. <br>
Risk: Returned note URLs may include full query parameters such as xsec_token. <br>
Mitigation: Preserve returned note URLs exactly when needed for traceability, and avoid sharing outputs with audiences that should not receive those full URLs. <br>
Risk: Research findings may overstate coverage because results are limited to the searched keyword and returned pages. <br>
Mitigation: State that analysis is based only on the current query and returned public result set, and avoid claiming complete platform coverage or deterministic traffic outcomes. <br>


## Reference(s): <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-content-research) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown research report with sample tables, content angles, interaction signals, reusable topic ideas, full note URLs, note IDs, and inline shell commands when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves returned note_url values exactly, including xsec_token query parameters; conclusions are limited to the current keyword and returned public result pages.] <br>

## Skill Version(s): <br>
0.1.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
