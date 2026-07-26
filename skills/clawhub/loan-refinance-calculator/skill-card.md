## Description: <br>
Calculates refinance savings, monthly payment changes, break-even timing, and recommendation details for loan refinancing scenarios using an API-backed pay-per-use service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and financial-service operators use this skill to compare existing and replacement loans, estimate savings after fees and penalties, and produce customer-facing refinance reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends loan details and an account key to an external API-backed service, and the security review notes that the default endpoint is plain HTTP. <br>
Mitigation: Use only with a trusted operator and a trusted secure API URL, and avoid sending sensitive customer loan data unless the service terms and transport security are acceptable. <br>
Risk: The security review reports that the included script currently has a syntax error. <br>
Mitigation: Review and test the script before relying on it for customer calculations or operational workflows. <br>
Risk: Refinance outputs are estimates and may not match bank approval results, actual fees, or regulatory constraints. <br>
Mitigation: Treat generated reports as decision support and confirm loan terms, compliance requirements, and financial advice with qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/loan-refinance-calculator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API result output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and REFINANCE_USER_KEY; calculations call an external API and consume account credits.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
