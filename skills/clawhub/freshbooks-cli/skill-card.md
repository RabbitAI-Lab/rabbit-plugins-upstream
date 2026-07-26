## Description: <br>
FreshBooks CLI for managing invoices, clients, and billing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haseebuchiha](https://clawhub.ai/user/haseebuchiha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage FreshBooks authentication, clients, invoices, billing lookups, invoice updates, archiving, and shareable invoice links through the FreshBooks CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI can create or modify FreshBooks clients, invoices, and billing records. <br>
Mitigation: Keep user confirmation in place before invoice or client changes and review JSON payloads before execution. <br>
Risk: FreshBooks OAuth credentials and tokens grant billing access if exposed or left on a shared machine. <br>
Mitigation: Install only from a trusted publisher, connect only intended FreshBooks accounts, and use the logout command when stored tokens should be removed. <br>


## Reference(s): <br>
- [FreshBooks CLI skill page](https://clawhub.ai/haseebuchiha/skills/freshbooks-cli) <br>
- [GitHub Package Registry for @haseebuchiha packages](https://npm.pkg.github.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI itself returns JSON to stdout for scripting and filtering.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
