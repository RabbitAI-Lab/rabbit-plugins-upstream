## Description: <br>
Manage NEAR Name Service (.near domains) - check availability, register, resolve, and manage names. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and NEAR users use this skill to check .near name availability, resolve names to account IDs, and initiate .near registrations from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted name or account inputs may execute unintended local shell commands during registration. <br>
Mitigation: Use only trusted inputs and avoid registration until the script validates input values and replaces shell-string execution with safe argument passing. <br>
Risk: Registration can submit a paid blockchain transaction that spends NEAR and may be hard to reverse. <br>
Mitigation: Treat register as a real transaction, review the target account and network before use, and avoid funded accounts until the registration path is reviewed. <br>


## Reference(s): <br>
- [NEAR Name Service](https://near.org/names/) <br>
- [NEAR CLI Documentation](https://docs.near.org/tools/near-cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/shaiss/skills/near-name-service) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command output and Markdown usage guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call NEAR RPC endpoints and invoke NEAR CLI for registration actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
