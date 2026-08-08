## Description: <br>
Runs a Telegram-based body-scan measurement workflow that submits a user-provided video to AnthroVision, manages consent and status polling, and returns deterministic measurements and waist-to-hip ratio output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to guide a Telegram body-measurement flow for consenting adult users, including input checks, scan submission, status polling, and structured measurement output. It is not intended for medical diagnosis, minors, non-consenting subjects, or multi-person videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local read, write, and exec powers. <br>
Mitigation: Narrow allowed powers to the AnthroVision body-scan bridge and remove local read, write, or exec access unless each operation is specifically justified and constrained. <br>
Risk: Body videos are highly sensitive and may be sent to an external processor. <br>
Mitigation: Require explicit consent and verify retention, deletion, data handling, and credential-scope policies before submitting any video. <br>
Risk: The server security verdict is suspicious because privacy scope and external bridge behavior are not sufficiently detailed. <br>
Mitigation: Review the skill before installation, document the external processing path, and deploy only after privacy and security controls are confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anthrovision-telegram-body-scan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown text with structured status fields and bullet lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes scan status, grouped body measurements, waist-to-hip ratio, timeout prompts, and input validation guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
