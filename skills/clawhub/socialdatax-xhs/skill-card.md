## Description: <br>
用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记，覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to retrieve and analyze Xiaohongshu / XHS / RedNote hot searches, notes, note details, comments, creator profiles, and creator note lists through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full Xiaohongshu note URLs may include xsec_token query parameters that can appear in agent outputs, saved reports, or transcripts. <br>
Mitigation: Share full tokenized URLs only with recipients who should receive them; use note IDs or sanitized links when exact tokenized URLs are not necessary. <br>
Risk: Runtime use requires a SocialDataX API key. <br>
Mitigation: Provide the key through SOCIALDATAX_API_KEY and avoid embedding it in generated files, command examples, or shared outputs. <br>


## Reference(s): <br>
- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Analysis] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON-formatted CLI/API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY plus node and npm; preserves full note URLs when exact returned links are needed.] <br>

## Skill Version(s): <br>
0.1.18 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
