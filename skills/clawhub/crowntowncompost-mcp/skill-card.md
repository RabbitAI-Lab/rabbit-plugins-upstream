## Description: <br>
Access the Crown Town Compost customer portal from a shell with curl to retrieve pickup history, invoices, service days, skips, and account details without running the crowntowncompost-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technically comfortable Crown Town Compost customers use this skill to script authenticated portal reads for service history, billing history, upcoming service days, and account details. The skill also documents live account write flows, which should be used only with explicit confirmation and follow-up verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes live account-changing portal actions such as skips, account updates, support messages, missed-pickup reports, and cancellation flows. <br>
Mitigation: Require explicit confirmation before any write action, then re-read the relevant portal page or endpoint to verify the account state. <br>
Risk: The skill can use a Crown Town Compost login and session cookie, which may expose account access on shared machines. <br>
Mitigation: Avoid storing credentials or cookie jars on shared systems, protect the cookie jar as sensitive data, and clear sessions when work is complete. <br>


## Reference(s): <br>
- [Crown Town Compost Portal Endpoint Reference](references/endpoints.md) <br>
- [Crown Town Compost Portal](https://portal.crowntowncompost.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell command examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces curl-based portal access instructions and examples; it does not run the portal actions by itself.] <br>

## Skill Version(s): <br>
0.3.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
