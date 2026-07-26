## Description: <br>
门诊病历内涵质控：高血压未记录血压最高值。给定门诊病历文本，调用内部医疗大模型，输出无缺陷或有缺陷及原因。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control teams and developers use this skill to check outpatient medical-record text for cases where hypertension is documented without a highest blood-pressure value. It returns a concise Chinese result indicating no defect or a defect with the reason. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes medical-record text and sends relevant clinical content to a configured LLM endpoint. <br>
Mitigation: Install and run it only in environments authorized for medical-record processing, de-identify records before use, and confirm the configured HiVoice MaaS or --base endpoint is approved for the data. <br>
Risk: Prepared text or output files can contain sensitive clinical information if saved in an unsecured location. <br>
Mitigation: Protect output directories, manage retention, and avoid --save-prepared unless the destination is secured. <br>
Risk: The result is an auxiliary quality-control signal, not a medical diagnosis or treatment recommendation. <br>
Mitigation: Require review by qualified clinical staff before using results in clinical or operational decisions. <br>
Risk: The skill requires an appkey for the external model service. <br>
Mitigation: Keep the appkey out of repositories and logs, and provide it only through approved secret-handling processes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-hypertension-missing-bp) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [UTF-8 text containing either 无缺陷 or 有缺陷 followed by a reason] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the result to a text file and prints the same quality-control result to standard output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
