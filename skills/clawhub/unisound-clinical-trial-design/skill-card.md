## Description: <br>
药企药物研发辅助临床试验设计辅助。参考 Clinical Trial Protocol Skill 的 protocol design 部分，构建药研方法设计能力。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinical development and pharmaceutical R&D users can use this skill to structure clinical trial design inputs and receive design review guidance for indication, intervention, phase, population, endpoints, and visit schedule. It supports method-design assistance only and does not replace ethics, regulatory, statistical, or clinical expert review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clinical trial design details and extracted document contents may be sent to a disclosed remote medical model API without enough privacy or scoping detail. <br>
Mitigation: Use only when approved to send the relevant study-design information to the remote API provider, and minimize input fields before use. <br>
Risk: Office, PDF, and image inputs can contain untrusted content and require local extraction or OCR tooling. <br>
Mitigation: Prefer JSON inputs; process other file types only in a constrained environment with required dependencies installed. <br>
Risk: Passing API keys directly on the command line may expose credentials through shell history or process inspection. <br>
Mitigation: Use short-lived credentials where possible and avoid placing long-lived API keys in command history. <br>
Risk: Generated clinical trial design guidance can be incomplete or inappropriate for a specific protocol. <br>
Mitigation: Require review by qualified statistical, medical, regulatory, and ethics experts before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-clinical-trial-design) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Clinical Trial Protocol Skill reference](https://agent-skills.md/skills/anthropics/healthcare/clinical-trial-protocol-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [UTF-8 JSON object containing structured trial design data and Markdown guidance text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires clinical trial design inputs and an appkey for the disclosed remote medical model API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
