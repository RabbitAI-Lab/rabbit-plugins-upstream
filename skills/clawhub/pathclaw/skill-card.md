## Description: <br>
通过华银康集团 PathClaw 服务对 .svs 病理切片进行 AI 辅助诊断。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[t-programmer](https://clawhub.ai/user/t-programmer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and clinical-support operators use this skill to submit a valid .svs pathology slide and selected pathology category to PathClaw for AI-assisted analysis. The result is framed as reference information that should be reviewed by qualified pathology professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads .svs pathology slides to an external PathClaw service, which may involve patient or regulated medical data. <br>
Mitigation: Use only when the user understands the external upload and the transfer is allowed by applicable privacy, consent, and data-governance requirements. <br>
Risk: AI-assisted pathology output may be mistaken for a final diagnosis. <br>
Mitigation: Keep the result advisory and require qualified clinicians to make final diagnostic decisions using clinical context and additional checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/t-programmer/skills/pathclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with tables, status summaries, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a readable .svs file path, one supported pathology category, upload to PathClaw, and polling for result status.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
