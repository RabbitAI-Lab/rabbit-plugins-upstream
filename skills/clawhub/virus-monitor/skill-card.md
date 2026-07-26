## Description: <br>
Monitors respiratory virus activity in Vienna by combining Austrian wastewater, Sentinel, and AGES data sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and public health analysts use this skill to retrieve and summarize Vienna-focused respiratory virus monitoring data from Austrian public data sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A separate virus-monitor executable could contact sources outside the documented Austrian public health data sites. <br>
Mitigation: Confirm the executable source before running it and verify that network access is limited to the documented data sites. <br>
Risk: Public health data may lag or update on a weekly cadence, so summaries may not reflect real-time conditions. <br>
Mitigation: Use the skill output as monitoring context and check source update timing before acting on results. <br>


## Reference(s): <br>
- [Nationales Abwassermonitoring](https://abwassermonitoring.at) <br>
- [MedUni Wien Sentinel System](https://viro.meduniwien.ac.at) <br>
- [AGES Abwasser Dashboard](https://abwasser.ages.at) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and JSON output structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces status levels and summarized source data for SARS-CoV-2, influenza, and RSV monitoring.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
