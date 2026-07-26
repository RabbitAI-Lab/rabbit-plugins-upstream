## Description: <br>
Generates Chinese similar-case retrieval reports for legal practitioners by collecting matter facts, using Deli Legal's CLI/API to retrieve candidate judgments, and organizing results into a standard report for court submission or internal strategy review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolalam](https://clawhub.ai/user/coolalam) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External legal professionals, court support staff, and in-house legal teams use this skill to turn pending-case facts, issues, venue context, and litigation purpose into a structured similar-case retrieval report. The report supports court submission or internal strategy review by summarizing retrieved cases, comparing facts and legal issues, and surfacing favorable and unfavorable authority. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive case facts, personal data, commercial information, or privileged legal material may be sent to an external Deli Legal CLI/API during retrieval. <br>
Mitigation: Redact unnecessary sensitive details before use, confirm before CLI calls, and share only the facts needed for retrieval. <br>
Risk: The Deli Legal API key is stored locally for CLI use and could expose access if mishandled. <br>
Mitigation: Treat the API key as a sensitive local credential, restrict machine access, and rotate or revoke it if exposure is suspected. <br>
Risk: Retrieved case data can be incomplete, stale, or missing fields, which may affect legal analysis or court submissions. <br>
Mitigation: Do not invent missing case fields; verify key cases through official sources before relying on the report for legal decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolalam/skills/case-retrieval-report) <br>
- [deli-cli common setup](artifact/references/cli-common.md) <br>
- [Similar-case retrieval CLI strategy guide](artifact/references/api-guide.md) <br>
- [Similar-case retrieval report template](artifact/references/report-template.md) <br>
- [Legal basis for similar-case retrieval](artifact/references/legal-basis.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with inline CLI commands and structured tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single similar-case retrieval report; case facts, court details, judgment metadata, and legal conclusions must come from user materials, CLI results, or later human verification.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter metadata is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
