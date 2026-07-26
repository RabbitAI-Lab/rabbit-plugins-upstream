## Description: <br>
Generates bid documents from uploaded tender files through the 百炼标书 API, including tender interpretation, editable DOCX bid generation, and compliance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and procurement teams use this skill to process authorized tender and bid files, generate editable bid documents, and review bid compliance through a third-party cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads procurement and bid files to the 百炼标书 cloud service, and those files or results may be retained under the user's App Key account. <br>
Mitigation: Use only files the user is authorized to process externally, and confirm the user is comfortable with cloud processing and retention before use. <br>
Risk: The App Key is an account credential and can be exposed through chat, screenshots, environment variables, or parameterized service links. <br>
Mitigation: Keep the App Key out of chat, store it only in the local config.json credential file, and avoid forwarding any links that contain credential parameters. <br>
Risk: ZCM_BASE, ZCM_CONFIG, ZCM_HOME, or ZCM_OUTPUT_DIR overrides can change the service endpoint or local credential and output paths. <br>
Mitigation: Review these overrides before execution and use the service only with expected paths and the declared 百炼标书 endpoint. <br>
Risk: Bid-document generation consumes credits from the App Key account. <br>
Mitigation: Check the account balance and confirm the user intends to spend credits before submitting generation tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite) <br>
- [Execution guide](references/usage.md) <br>
- [API contract reference](references/api.md) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files, Markdown] <br>
**Output Format:** [Markdown guidance with local DOCX, HTML, Word, and JSON-backed task outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local App Key configuration and can produce report or bid-document files under the configured output directory.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
