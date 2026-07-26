## Description: <br>
Provides a Chinese-language fortune-telling persona for Bazi and Ziwei life readings and Liuyao event readings, using structured local charting and validation materials while keeping the user-facing response conversational. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users can use this skill for Chinese-style reflective fortune-telling conversations about long-term life themes or one concrete event question. Agents use it to gather calendar, birth, location, or event details, generate a calibrated reading, and return concise Chinese guidance without exposing internal reasoning traces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask users for birth details, location, and time zone for charting. <br>
Mitigation: Collect only details needed for the current reading and avoid retaining or reusing sensitive personal data outside the conversation. <br>
Risk: Fortune-telling output may be mistaken for medical, legal, financial, safety, or other professional advice. <br>
Mitigation: Frame results as reflective or entertainment content and route high-stakes decisions to qualified professionals. <br>
Risk: Implicit invocation is enabled for related topics, which can trigger the persona in broad fortune-telling contexts. <br>
Mitigation: Confirm the user's intent before gathering sensitive details or producing a reading. <br>


## Reference(s): <br>
- [Skill source](artifact/SKILL.md) <br>
- [命理会谈方法](artifact/references/consultation-method.md) <br>
- [内部会谈计划](artifact/references/consultation-plan-schema.md) <br>
- [内部推断方法](artifact/references/interpretation-method.md) <br>
- [六爻问事方法](artifact/references/liuyao-method.md) <br>
- [六爻会谈计划](artifact/references/liuyao-plan-schema.md) <br>
- [算命老师傅的核心身份](artifact/references/master-identity.md) <br>
- [人味与深沉表达](artifact/references/voice-and-dialogue.md) <br>
- [紫微解释来源](artifact/references/ziwei-sources.md) <br>
- [APA Barnum effect](https://dictionary.apa.org/barnum-effect) <br>
- [GenAI fortune-telling trust and feedback study](https://arxiv.org/abs/2603.27784) <br>
- [ziwei.my public Ziwei learning material](https://www.ziwei.my/) <br>
- [blader/humanizer](https://github.com/blader/humanizer) <br>
- [Yiqi-BaZi-ZiWei upstream](https://github.com/fdxuyq/Yiqi-BaZi-ZiWei) <br>
- [mingyu-core upstream](https://github.com/Brhiza/mingyu) <br>
- [tyme4ts upstream](https://github.com/6tail/tyme4ts) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Chinese conversational text with optional Markdown Liuyao tables and JSON chart or validation artifacts for agent use.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires birth details for life readings or a concrete event question for Liuyao; outputs should be treated as reflective or entertainment content.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
