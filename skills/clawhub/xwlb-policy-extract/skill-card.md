## Description: <br>
新闻联播政策摘要获取每日《新闻联播》文字稿，提取宏观经济政策和可能影响金融市场走向的政策内容，并生成分级摘要。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhutulang](https://clawhub.ai/user/zhutulang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, financial analysts, and policy watchers use this skill to summarize Xinwen Lianbo transcripts and identify macroeconomic, industrial, regional, and financial-market policy signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create a temporary transcript file while preparing the parser input. <br>
Mitigation: Use a temporary working location, avoid storing sensitive user material in the transcript file, and delete the file after parsing. <br>
Risk: The broad trigger term "国家政策" may activate the skill when the user intended a different policy workflow. <br>
Mitigation: Confirm the target date and that the user wants a Xinwen Lianbo policy summary before fetching or parsing transcript content. <br>


## Reference(s): <br>
- [Macro Policy Keyword Reference](artifact/references/macro_keywords.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zhutulang/skills/xwlb-policy-extract) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown policy summary report, with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Classifies transcript items into tier1, tier2, and tier3 policy relevance using keyword matching.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
