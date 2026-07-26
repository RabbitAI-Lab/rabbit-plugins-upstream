## Description: <br>
PIPL-Compliance helps agents run local PIPL compliance self-checks, risk assessments, report generation, and draft document generation for Chinese personal information protection workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, compliance teams, and organizations handling China PIPL workflows use this skill as a local self-check and drafting aid for compliance scenarios, risk assessment, reports, and privacy document templates. The outputs are reference materials and should be reviewed by qualified counsel before legal or regulatory use. <br>

### Deployment Geography for Use: <br>
China-focused PIPL use cases; review requirements before applying the outputs in other jurisdictions. <br>

## Known Risks and Mitigations: <br>
Risk: Users may over-rely on generated compliance checks or documents as legal advice. <br>
Mitigation: Treat outputs as local drafting and self-check aids and require review by qualified counsel before legal, business, or regulatory use. <br>
Risk: Report and document generation can write files to local output paths. <br>
Mitigation: Review requested output paths before execution and run the skill in a workspace where generated files are expected. <br>
Risk: Dependency resolution may vary because Jinja2 is specified as a minimum version. <br>
Mitigation: Pin Jinja2 exactly in controlled deployments when reproducible installs are required. <br>


## Reference(s): <br>
- [PIPL Compliance Skill Documentation](SKILL.md) <br>
- [PIPL Compliance README](README.md) <br>
- [PIPL Law Summary Guide](references/pipl-law.md) <br>
- [PIPL Compliance Checklist](references/pipl-checklist.md) <br>
- [China PIPL Compliance Checklist](references/cn-checklist.md) <br>
- [PIPL Risk Assessment Guide](references/risk-assessment-guide.md) <br>
- [PIPL Enforcement Cases](references/enforcement-cases.md) <br>
- [Chinese Privacy Policy Template](assets/templates/privacy-policy-cn.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, HTML, CSV] <br>
**Output Format:** [Markdown guidance with shell commands, plus generated JSON, Markdown, HTML, CSV, and document template files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally; report and document tools can write files to user-selected local output paths.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence; artifact package.json and CHANGELOG list 1.2.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
