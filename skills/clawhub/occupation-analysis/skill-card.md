## Description: <br>
Occupation Analysis helps vocational education teams generate structured occupation analysis reports for secondary vocational, higher vocational, and vocational undergraduate programs using a work-process curriculum development method. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Vocational education curriculum developers and professional program teams use this skill to analyze occupations, extract typical work tasks, define action and learning domains, and produce structured curriculum-development reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests root-level package installation for Pandoc. <br>
Mitigation: Install dependencies in a controlled environment and review package sources before allowing sudo package installation. <br>
Risk: The artifact includes weak guidance around IMA credential handling. <br>
Mitigation: Provide IMA credentials through a secure environment or secret manager, and do not commit or share .env files. <br>
Risk: Generated occupation analysis can be incorrect if occupation data, education level, or local reference assets are missing or mismatched. <br>
Mitigation: Run the precheck workflow, require user confirmation of occupation information, and review the final report against authoritative vocational data before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flyboat403/skills/occupation-analysis) <br>
- [Server-Resolved GitHub Provenance](https://github.com/flyboat403/occupation-analysis) <br>
- [Work Process Method](references/work_process_method.md) <br>
- [Workflow Details](references/workflow_details.md) <br>
- [Report Template](references/report_template.md) <br>
- [Analysis Data Template](references/analysis_data_template.json) <br>
- [Precheck Guide](references/precheck_guide.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, Word document outputs, JSON analysis data, and setup or validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a seven-part vocational analysis report and supporting structured data; report quality depends on confirmed occupation data and available local reference assets.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
