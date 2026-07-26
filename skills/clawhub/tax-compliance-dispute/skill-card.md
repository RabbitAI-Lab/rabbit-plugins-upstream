## Description: <br>
Provides China-focused tax compliance and dispute guidance for internal controls, liquidation and deregistration, tax audits, administrative remedies, contract tax clauses, invoice compliance, and tax-related criminal risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance and tax teams, compliance reviewers, and advisors use this skill to identify China tax compliance risks, prepare dispute-response paths, and generate practical self-check guidance. The skill is advisory and should be reviewed against current authority and professional judgment for material matters. <br>

### Deployment Geography for Use: <br>
Global for China tax compliance and dispute contexts <br>

## Known Risks and Mitigations: <br>
Risk: Tax and compliance inputs may be sent to mcp.aitaxs.top and, during fallback, potentially to public search engines. <br>
Mitigation: Avoid submitting sensitive personal, taxpayer, credential, or confidential business data unless that transfer is approved for the intended use. <br>
Risk: The package includes local credential storage behavior for service access. <br>
Mitigation: Review where credentials are stored, protect the local profile directory, and rotate or remove keys when access is no longer needed. <br>
Risk: Helper scripts can alter client configuration files when automatic setup is enabled. <br>
Mitigation: Review or disable TAX_ENABLE_AUTOSETUP before running MCP helper scripts, and inspect configuration backups or diffs after setup. <br>
Risk: The matrix install command can modify the user-level skills directory by installing related packages. <br>
Mitigation: Run the matrix installer only when bulk installation is intended, and review the target skill paths before use. <br>
Risk: Tax, audit, dispute, and criminal-risk guidance can become outdated or may not fit a specific case. <br>
Mitigation: Verify material conclusions against current official sources and consult a qualified tax professional or lawyer for high-stakes matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Interactive compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance with optional checklists, report outlines, code snippets, shell commands, configuration changes, and web links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory responses and self-check artifacts; material tax, legal, or dispute conclusions require review against current official sources and qualified professionals.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
