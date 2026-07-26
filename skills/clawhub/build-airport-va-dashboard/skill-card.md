## Description: <br>
Generate, rebuild, or update a single-file Smart Airport video-analytics HTML dashboard from face-record Excel workbooks, with filters, charts, comparison metrics, data-quality reporting, and in-browser Excel upload. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haixiandaxia-jpg](https://clawhub.ai/user/haixiandaxia-jpg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations analysts use this skill to create a local, browser-based airport video-analytics dashboard from face-record Excel workbooks. It helps inspect traffic, demographics, camera coverage, comparison periods, and data quality without requiring a backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Airport face-record Excel workbooks may contain sensitive or regulated data. <br>
Mitigation: Use only data you are authorized to analyze, and keep workbook processing local unless a backend is explicitly requested and reviewed. <br>
Risk: Generated dashboards may depend on CDN-loaded libraries if fully embedded libraries are not feasible. <br>
Mitigation: Prefer embedded libraries for offline use, or disclose and review CDN dependencies before using the dashboard in restricted environments. <br>


## Reference(s): <br>
- [Airport VA dashboard contract](references/dashboard-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [HTML file with concise Markdown handoff notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single browser-openable dashboard and recommends local validation with python3 scripts/validate_dashboard.py.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
