## Description: <br>
用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve structured details for a Douyin work from an aweme ID, content URL, short link, or share text. It supports content research and social data analysis by returning factual fields such as title, author, publish time, interaction counts, images, video, music, and media summaries when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Douyin IDs, URLs, share text, and the SOCIALDATAX_API_KEY are sent to SocialDataX services for detail lookups. <br>
Mitigation: Use the skill only with data you are allowed to share, keep the API key in the environment, and use the official SocialDataX AI access page for key management. <br>
Risk: The documented direct CLI examples use socialdatax-skills@latest, so package behavior can change between runs. <br>
Mitigation: Pin the npm package version when repeatable behavior is required. <br>
Risk: Optional media download commands can write returned media assets to local storage. <br>
Mitigation: Choose an explicit output path or directory and review saved media before reuse or redistribution. <br>


## Reference(s): <br>
- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON data returned by SocialDataX tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY, node, and npm for direct CLI calls; optional media downloads write only to the requested local output path or directory.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
