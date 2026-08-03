## Description: <br>
Generate monthly and annual operations reports from IMRC system data across 10 configured pages, with optional Meixin message summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations analysts use this skill to extract or organize IMRC operations data, combine it with Meixin collaboration updates, and produce structured monthly or annual reporting drafts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reports can appear authoritative while using hard-coded or placeholder figures. <br>
Mitigation: Replace placeholder values or label them clearly, then verify all metrics against IMRC source systems before distribution. <br>
Risk: The skill summarizes internal IMRC data and Meixin messages, including team and personnel information. <br>
Mitigation: Run the skill only with authorized access and share generated reports only with approved internal audiences. <br>
Risk: Extraction scripts currently simulate or stage data capture rather than proving live source completeness. <br>
Mitigation: Confirm the generated JSON contains complete current source data before using the executive summary or section reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/imrc-report) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [IMRC page configuration](artifact/config/pages.json) <br>
- [Report template](artifact/config/report_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with supporting JSON extraction files and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated reports may include internal operational metrics and personnel-related message summaries; verify source data before sharing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
