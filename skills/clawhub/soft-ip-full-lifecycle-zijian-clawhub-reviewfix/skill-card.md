## Description: <br>
Software IP self-assessment skill that provides an AI-delivered compliance review for Chinese software copyright applications, covering material completeness, source-code documentation, user manuals, rights attribution, registration readiness, and clawtip payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users preparing Chinese software copyright applications use this skill after clawtip payment to receive an AI-delivered diagnostic review of application materials, source-code documentation, user manuals, rights attribution, and registration readiness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a local order file that includes the user's initial question. <br>
Mitigation: Keep the initial question brief and omit source code, trade secrets, applicant details, and confidential legal facts unless local storage is acceptable. <br>
Risk: The service is gated by clawtip payment verification before the assessment is authorized. <br>
Mitigation: Confirm clawtip is installed and complete payment verification before relying on the service output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/soft-ip-full-lifecycle-zijian-clawhub-reviewfix) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown assessment report plus shell command output with JSON_RESULT status lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires clawtip payment verification and creates a local order file containing payment fields and the initial question.] <br>

## Skill Version(s): <br>
3.1.38 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
