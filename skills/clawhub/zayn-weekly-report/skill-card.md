## Description: <br>
Analyzes weekly work records, project outcomes, result density, waiting items, closure ability, and resource allocation to identify stalled work and produce focused goals and management decisions for the next week. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, managers, and operations or sales teams use this skill to turn weekly reports, daily records, project status, and support needs into a structured weekly review. It separates activity from outcomes, identifies stalled or waiting work, and proposes 3 to 5 verifiable result-oriented goals for the next week. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Weekly work records and business reporting data may contain sensitive commercial or operational details. <br>
Mitigation: Provide only the report data the agent needs to analyze, and avoid including unrelated confidential material. <br>
Risk: Incomplete weekly inputs can lead to qualitative conclusions instead of reliable metrics. <br>
Mitigation: Treat missing or unsupported counts as data gaps and avoid calculating ratios when numerator or denominator evidence is unreliable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zaynpeng/skills/zayn-weekly-report) <br>
- [Artifact README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Structured Markdown report with summaries, tables, prioritized goals, and decision items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not calculate result density or conversion ratios unless the required source counts are reliable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact README and changelog list v0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
