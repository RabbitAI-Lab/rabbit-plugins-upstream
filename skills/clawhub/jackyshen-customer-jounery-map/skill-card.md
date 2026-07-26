## Description: <br>
Generates consulting-style customer, employee, or service journey maps from structured YAML or touchpoint data as SVG, PNG, and PDF exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mebusw](https://clawhub.ai/user/mebusw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, service designers, and consultants use this skill to turn staged journey data into professional journey-map deliverables for customer, employee, service, or stakeholder experiences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create or overwrite local journey_map.svg, journey_map.png, and journey_map.pdf files. <br>
Mitigation: Specify output filenames or review the workspace before running exports when existing files must be preserved. <br>
Risk: PNG and PDF export may invoke Playwright or Chromium. <br>
Mitigation: Run exports in an environment where browser automation is expected and restrict output formats when only SVG is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/jackyshen-customer-jounery-map) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Guidance] <br>
**Output Format:** [SVG, PNG, and PDF files with supporting YAML-oriented guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or overwrite journey_map.svg, journey_map.png, and journey_map.pdf in the workspace] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
