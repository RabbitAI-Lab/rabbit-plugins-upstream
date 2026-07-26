## Description: <br>
Analyzes a specific bidding opportunity before submission, using bid-history data to produce a pre-bid due-diligence report with buyer profile, competitive landscape, price benchmarks, risk flags, and bid/no-bid guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business-development teams use this skill to evaluate whether and how to bid on a concrete procurement project. It produces a decision-oriented pre-bid analysis from public bidding records, user-provided project details, and vendor API results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Consent-based trial registration can send a hashed MAC-derived device identifier for trial de-duplication. <br>
Mitigation: Use a preconfigured ZLBX_API_KEY to bypass registration, or decline auto-registration unless the user accepts the vendor workflow. <br>
Risk: The skill can persist an API key in a local configuration file. <br>
Mitigation: Protect ~/.zlbx/config.json on shared machines and rotate or revoke the key if local access may have been exposed. <br>
Risk: Generated HTML reports and copied source links may contain signed access parameters. <br>
Mitigation: Treat reports and links as sensitive, share them only with the intended audience, and redact signed URLs before broader distribution. <br>
Risk: Reports are written to the user's home directory. <br>
Mitigation: Review the saved report path and contents before sharing, and remove generated files when they are no longer needed. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant) <br>
- [Workflow guide](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration workflow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown decision report plus optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based trial registration; full reports typically use 12-25 vendor API queries and may include signed source links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
