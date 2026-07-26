## Description: <br>
Reviews IPO filing materials such as prospectuses, inquiry responses, and financial statement notes by running a local tool for financial-data consistency, cross-file differences, table arithmetic checks, evidence locations, and report interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangbotaochn](https://clawhub.ai/user/wangbotaochn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and review teams use this skill to run a local IPO filing review workflow over PDF, DOCX, XLSX, and TXT materials, then interpret generated issues, diagnostics, and evidence locations. It is intended to support numeric and disclosure consistency review, not replace professional judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IPO filing inputs and generated outputs can contain sensitive financial facts and source snippets. <br>
Mitigation: Run the tool only in a trusted local environment and protect the output directory. <br>
Risk: Automated review can miss semantic or narrative disclosure issues and may produce items that need human confirmation. <br>
Mitigation: Use the generated report as a review aid, prioritize key issues, and keep professional manual review in the workflow. <br>
Risk: Open dependency ranges can make installations less reproducible over time. <br>
Mitigation: Pin dependency versions before controlled or production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wangbotaochn/skills/ipo-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; the bundled local tool generates HTML, JSON, CSV, and TXT files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated outputs may include extracted financial facts, evidence locations, source snippets, diagnostic CSVs, and run logs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
