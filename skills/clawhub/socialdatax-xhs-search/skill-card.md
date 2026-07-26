## Description: <br>
用于小红书数据分析、小红书笔记搜索、关键词检索、内容调研、竞品分析和趋势研究。覆盖 Xiaohongshu / XHS / RedNote note search，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to search Xiaohongshu / XHS / RedNote notes by keyword for content research, competitor analysis, market observation, and trend scanning through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends XHS search queries and the SOCIALDATAX_API_KEY to SocialDataX. <br>
Mitigation: Use the skill only with an API key and queries that are appropriate to share with SocialDataX. <br>
Risk: Returned note_url values may include xsec_token query parameters that are preserved in outputs. <br>
Mitigation: Review exported, forwarded, or published results before sharing them outside the intended audience. <br>
Risk: Search results are bounded by requested pages and filters, so they may not represent complete platform coverage. <br>
Mitigation: Describe results as based on fetched pages and keep visible evidence separate from interpretation. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-search) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and search-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search outputs may include full note_url values with xsec_token query parameters and complete 24-character note_id values.] <br>

## Skill Version(s): <br>
0.1.14 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
