## Description: <br>
Occupation Analysis helps agents create vocational education occupation-analysis reports using work-process curriculum development methods for secondary, higher vocational, and vocational undergraduate programs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Education developers, curriculum designers, and agents use this skill to analyze professional teaching standards and occupation data, derive job tasks and learning fields, and generate structured vocational education occupation-analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged installation guidance may change the host system. <br>
Mitigation: Install in a contained environment and avoid the sudo Pandoc install step unless the package is trusted and Word export is required. <br>
Risk: Broad dependency installation can introduce unnecessary package exposure. <br>
Mitigation: Review or trim requirements.txt before installing dependencies. <br>
Risk: PDF fetching or parsing can expose the workflow to untrusted network content. <br>
Mitigation: Use --no-pdf when PDF parsing is not needed, or restrict PDF URLs to trusted official sources. <br>
Risk: Local credential files can expose live API keys if mishandled. <br>
Mitigation: Do not place live API keys in .env unless the file is excluded from version control and protected. <br>


## Reference(s): <br>
- [Work Process Method](artifact/references/work_process_method.md) <br>
- [Workflow Details](artifact/references/workflow_details.md) <br>
- [Analysis Data Template](artifact/references/analysis_data_template.json) <br>
- [Occupation Mapping Template](artifact/references/occupation_mapping_template.json) <br>
- [Report Template](artifact/references/report_template.md) <br>
- [Precheck Guide](artifact/references/precheck_guide.md) <br>
- [Troubleshooting Guide](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON intermediate data, shell commands, and optional Word documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate Markdown and Word report files after local dependency and Pandoc setup.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; SKILL.md frontmatter lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
