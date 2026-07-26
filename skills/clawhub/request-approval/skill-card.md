## Description: <br>
Use Preloop's request_approval tool to get human approval before risky operations like deletions, production changes, or external modifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yconst](https://clawhub.ai/user/yconst) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to require human approval before agents carry out destructive, sensitive, production, financial, security, or external-system operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The approval workflow depends on the Preloop MCP endpoint, authentication, and approval policy being configured correctly. <br>
Mitigation: Verify the endpoint and package before installation, store a dedicated least-privilege token securely, and confirm an approval policy is active. <br>
Risk: An agent could reduce the value of human oversight by making vague approval requests or continuing after denial or timeout. <br>
Mitigation: Request approval before execution with specific operation, context, and reasoning details, and treat denial or timeout as a stop condition. <br>


## Reference(s): <br>
- [Setup & Configuration](references/SETUP.md) <br>
- [Detailed Examples](references/EXAMPLES.md) <br>
- [Troubleshooting](references/TROUBLESHOOTING.md) <br>
- [Preloop Documentation](https://docs.preloop.ai) <br>
- [Preloop GitHub Repository](https://github.com/preloop/preloop) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with structured approval request fields and inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured Preloop MCP server and approval policy; denied or timed-out approvals stop the risky operation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
