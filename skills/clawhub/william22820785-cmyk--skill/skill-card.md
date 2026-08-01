## Description: <br>
A Chinese-language fortune-telling conversation skill that adopts a seasoned master persona for life readings and concrete event divination, using packaged consultation methods and validation scripts to produce concise user-facing judgments while hiding internal reasoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
External users use this skill for Chinese-language conversational fortune-telling about life themes, relationships, work, wealth, timing, and specific outcomes. Agents use it to gather required context, run local divination-support scripts when applicable, validate responses, and return short Markdown/plain-text readings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a strong fortune-teller persona and asks the agent to conceal its AI nature. <br>
Mitigation: Review the persona requirements before use and disclose agent identity when required by policy, platform rules, or user expectations. <br>
Risk: The skill may store hidden local consultation artifacts while producing readings. <br>
Mitigation: Run it only in an approved workspace and review or remove generated local artifacts after the session. <br>
Risk: The skill runs unpackaged local code and may depend on local skill-directory resources. <br>
Mitigation: Inspect and scan scripts and local dependencies before installation or execution, and run them in a constrained environment. <br>
Risk: Fortune-telling output can influence sensitive health, legal, financial, or relationship choices. <br>
Mitigation: Treat readings as non-professional guidance and require independent judgment or qualified professional advice for high-stakes decisions. <br>


## Reference(s): <br>
- [Skill release page](https://clawhub.ai/william22820785-cmyk/skills/skill) <br>
- [Publisher profile](https://clawhub.ai/user/william22820785-cmyk) <br>
- [命理会谈方法](references/consultation-method.md) <br>
- [算命老师傅的核心身份](references/master-identity.md) <br>
- [内部推断方法](references/interpretation-method.md) <br>
- [六爻问事方法](references/liuyao-method.md) <br>
- [内部会谈计划](references/consultation-plan-schema.md) <br>
- [六爻+奇门双法会谈计划](references/liuyao-plan-schema.md) <br>
- [Yiqi-BaZi-ZiWei upstream](https://github.com/fdxuyq/Yiqi-BaZi-ZiWei) <br>
- [mingyu-core upstream](https://github.com/Brhiza/mingyu) <br>
- [tyme4ts upstream](https://github.com/6tail/tyme4ts) <br>
- [Barnum Effect](https://dictionary.apa.org/barnum-effect) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Chinese conversational text or Markdown, with JSON artifacts and shell commands used internally when scripts are run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local consultation, fusion, chart, plan, and response files during execution; final user-facing output should avoid exposing internal reasoning artifacts.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
