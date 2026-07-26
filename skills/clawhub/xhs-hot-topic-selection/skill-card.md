## Description: <br>
用于小红书热榜选题、小红书热点选题、小红书热榜分析、小红书热点分析和趋势选题参考，帮助把当前热榜信号和热门笔记样本整理成可执行选题。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and social media operators use this skill to review current Xiaohongshu / XHS / RedNote hot-list signals, inspect related public note samples, and turn those signals into topic candidates, title hooks, content angles, and next-step planning guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SocialDataX API key for data access. <br>
Mitigation: Confirm the user is comfortable providing the API key through the SOCIALDATAX_API_KEY environment variable before use. <br>
Risk: Returned full note URLs can be sensitive sharing artifacts. <br>
Mitigation: Preserve note URLs exactly when needed, and avoid forwarding or storing them outside the user's intended workflow. <br>
Risk: Hot-list and note-sample analysis may be incomplete or time-bound. <br>
Mitigation: Present findings as current signals from returned public results, not as complete platform coverage or guaranteed traffic outcomes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection) <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with optional shell command examples and structured topic analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include current hot-list signals, topic candidates, public note samples, title hooks, content angles, hotspots to avoid, next-step recommendations, and full note URLs returned by the data source.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
