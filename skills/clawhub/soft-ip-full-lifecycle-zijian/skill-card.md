## Description: <br>
Software intellectual property full lifecycle self-assessment for Chinese software copyright applications, covering material completeness review, compliance verification, and registration readiness audit while using a third-party ClawTip service for order creation and payment verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers preparing Chinese software copyright applications use this skill to check source-code documentation, user manuals, rights documentation, and overall submission readiness before filing. The skill is designed to produce local self-assessment guidance and issue lists, with paid access verified through ClawTip. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The initial question is sent to a third-party order service during order creation. <br>
Mitigation: Do not include source code, contracts, company secrets, personal identifiers, or other sensitive material in the initial question. <br>
Risk: Payment and order metadata is stored locally in the user's OpenClaw orders directory. <br>
Mitigation: Review and remove local order files after use when retention is not needed. <br>
Risk: The skill requires network access and third-party payment verification before service delivery. <br>
Mitigation: Review the printed data-transfer notices before running order creation or verification commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/soft-ip-full-lifecycle-zijian) <br>
- [Third-party order and verification service](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown guidance with command-line status output for order creation and payment verification.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The service flow depends on a valid ClawTip order and may store order metadata locally under the user's OpenClaw orders directory.] <br>

## Skill Version(s): <br>
3.1.39 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
