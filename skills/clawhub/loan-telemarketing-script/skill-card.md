## Description: <br>
Generates customized loan telemarketing scripts from product and customer-profile inputs, including opening hooks, value framing, needs discovery, product presentation, objection handling, and closing language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Loan assistance sales teams and operators use this skill to draft call scripts for consumer loans, business loans, mortgage-related loans, and other lending scenarios. Users should review generated scripts against financial advertising, telemarketing, data-protection, and local compliance requirements before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A third-party pay-per-use backend receives prompt data and a user key. <br>
Mitigation: Use only non-sensitive sample or approved business inputs; do not enter real customer PII, account numbers, contact lists, or confidential financial records. <br>
Risk: The security evidence reports that the skill sends data to an insecure remote HTTP service. <br>
Mitigation: Install only if this data flow is acceptable for the environment; avoid sensitive inputs unless the publisher moves the service to HTTPS on a named trusted host. <br>
Risk: The documentation and code disagree about the generator command and backend behavior. <br>
Mitigation: Inspect the installed script before use and follow the actual CLI exposed by the artifact until the publisher aligns the documentation and implementation. <br>
Risk: Generated loan solicitation scripts may be inaccurate, noncompliant, or unsuitable for a specific jurisdiction or institution. <br>
Mitigation: Review all scripts with qualified compliance staff and adapt them to applicable financial, telemarketing, privacy, and company policies before calls are made. <br>


## Reference(s): <br>
- [Opening Hooks Reference](references/opening_hooks.md) <br>
- [Objection Handling Reference](references/objection_handling.md) <br>
- [Compliance Rules Reference](references/compliance_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, guidance] <br>
**Output Format:** [JSON from the generator command, containing generated telemarketing-script text and account status details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TELE_SCRIPT_USER_KEY; generated scripts may require human compliance review before use.] <br>

## Skill Version(s): <br>
1.2.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
