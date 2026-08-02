## Description: <br>
A Chinese-language fortune-telling persona skill that conducts Bazi/Ziwei life readings and Liuyao/Qimen event consultations, collecting birth details or question context and returning concise conversational judgments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william22820785-cmyk](https://clawhub.ai/user/william22820785-cmyk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for Chinese fortune-telling conversations about life patterns, relationships, career, wealth, and specific decisions. It should be treated as entertainment or reflective guidance and not relied on for medical, legal, financial, relationship-crisis, or other major decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill hides its AI or process framing and can present confident guidance on sensitive life topics. <br>
Mitigation: Deploy it only with clear user expectations that outputs are entertainment or reflective guidance, and do not use it for medical, legal, financial, relationship-crisis, or other major decisions. <br>
Risk: The skill may collect birth details or personal situations that can be written to local files. <br>
Mitigation: Collect only the minimum needed information, avoid unnecessary identifiers, and handle generated local files as sensitive user data. <br>
Risk: The security review notes that lunar-date support appears inaccurate in the submitted script. <br>
Mitigation: Confirm calendar inputs with the user and avoid relying on lunar-date calculations for consequential decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/william22820785-cmyk/skills/skill) <br>
- [License](LICENSE) <br>
- [Third-party notices](NOTICE) <br>
- [命理会谈方法](references/consultation-method.md) <br>
- [六爻问事方法](references/liuyao-method.md) <br>
- [话术语气细则](references/voice-and-dialogue.md) <br>
- [APA Barnum effect](https://dictionary.apa.org/barnum-effect) <br>
- [NIDA OARS communication techniques](https://nida.nih.gov/sites/default/files/oarsessentialcommunicationtechniques.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese conversational text and Markdown, with occasional command examples for internal validation workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request birth details, location/time context, or three numbers for divination-style consultations; local files may be used by the skill's scripts.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
