## Description: <br>
Provides code quality audit, vulnerability scanning, dependency security analysis, and test strategy guidance while sending user question text and encrypted payment verification data to api.ideaidea.com.cn for paid order creation and fulfillment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security-minded teams use this skill to request Chinese-language code security review, dependency risk analysis, secure coding recommendations, and test strategy guidance. It is suited for pre-release security review and remediation planning when users accept the paid verification workflow and external disclosure boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User question text and encrypted payment verification data are sent to api.ideaidea.com.cn. <br>
Mitigation: Avoid putting source code, secrets, vulnerability details, private project information, or other sensitive content in the question text unless external disclosure is acceptable. <br>
Risk: Server evidence reports inconsistent privacy wording and a suspicious security verdict. <br>
Mitigation: Confirm the data handling disclosures before deployment and align user-facing wording with the actual external verification behavior. <br>
Risk: Server guidance says the service script is broken before relying on the paid workflow. <br>
Mitigation: Fix and retest the service fulfillment script before using the paid verification flow in production. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/qa-security) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [External verification service](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown or plain-text security review with remediation guidance and command examples; payment scripts also emit key-value status lines and JSON_RESULT output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires clawtip payment verification; user question text and encrypted payment credential data are sent to the external verification service.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release metadata; artifact frontmatter metadata.version is 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
