## Description: <br>
Generate PPT with Baidu Wenku AI. Smart template selection based on content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ide-rea](https://clawhub.ai/user/ide-rea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to generate Baidu Wenku AI presentation decks from a topic, optionally selecting a template style or letting the skill choose one based on the prompt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Presentation prompts and supplied web content are sent to Baidu for processing. <br>
Mitigation: Avoid confidential, regulated, or proprietary material unless Baidu's terms and organizational policy allow it. <br>
Risk: The skill depends on a Baidu API credential. <br>
Mitigation: Keep BAIDU_API_KEY scoped, protected, and available only in the execution environment that needs it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ide-rea/skills/ai-ppt-generator) <br>
- [Baidu Qianfan AI PPT API endpoint](https://qianfan.baidubce.com/v2/tools/ai_ppt/) <br>
- [Baidu Qianfan PPT theme endpoint](https://qianfan.baidubce.com/v2/tools/ai_ppt/get_ppt_theme) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON status output containing the generated PPT URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and BAIDU_API_KEY; generation may take several minutes and streams status until completion.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
