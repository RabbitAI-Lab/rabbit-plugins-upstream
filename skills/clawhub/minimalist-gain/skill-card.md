## Description: <br>
Reports what minimalist actually measured in the current session or project, including LOC avoided, scope rejected, and dependencies declined. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[divyeshjayswal](https://clawhub.ai/user/divyeshjayswal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run the repository's persisted rejection-ledger report and present measured or logged savings data without adding unsupported estimates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may execute a repo-local report command in the current repository. <br>
Mitigation: Install and use it only in repositories where the report script is trusted, and review the command before execution. <br>
Risk: Logged lines avoided can be mistaken for measured hard numbers. <br>
Mitigation: Keep the estimate label attached and report the ledger output without restating estimates as measured values. <br>
Risk: Missing scripts or empty ledgers could lead to unsupported fallback claims. <br>
Mitigation: State plainly when the script or data is missing and do not extrapolate costs, percentages, or savings. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Markdown or plain text report based on the repo-local command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves labels for estimates and reports missing scripts or empty ledgers plainly.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
