## Description: <br>
Run a two-role worker/reviewer loop that implements, verifies, independently reviews, and reconciles code changes before returning them to the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[h0ngcha0](https://clawhub.ai/user/h0ngcha0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use Hubo for programming tasks where one agent implements changes and an independent reviewer challenges the implementation until findings are fixed, withdrawn, or escalated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The designated work agent may edit project files after explicit activation. <br>
Mitigation: Invoke the skill only for concrete programming tasks and review the reported diff, decisions, and verification before accepting the result. <br>
Risk: The final transcript can expose task details, command output, or sensitive content supplied during the work. <br>
Mitigation: Follow the workflow's redaction rule for credentials, secrets, and system-protected data before final handoff. <br>
Risk: Unsupported or mismatched host adapter capabilities can weaken the intended worker/reviewer separation. <br>
Mitigation: Select exactly one supported host adapter from the tools actually exposed, and ask the user before falling back when two resumable roles cannot be created. <br>


## Reference(s): <br>
- [Complete Hubo workflow](workflow.md) <br>
- [Supported host adapters](references/hosts.md) <br>
- [ClawHub skill page](https://clawhub.ai/h0ngcha0/skills/hubo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown conversation reports with code, command results, review findings, and a final chronological transcript] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a worker/reviewer exchange in the conversation; the workflow says not to store the transcript in a file.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
