## Description: <br>
Analyzes JDK GC logs and produces formal HTML reports plus concise Markdown summaries for performance review, stakeholder reporting, and JVM tuning decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ranenwang](https://clawhub.ai/user/ranenwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, performance engineers, and technical leaders use this skill to analyze one or more JVM GC log files, identify pause, Full GC, heap pressure, and data-completeness issues, and turn the findings into executive-ready and architect-ready reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GC logs and JVM parameters can expose operational details in generated HTML or Markdown reports. <br>
Mitigation: Review and redact generated reports before sharing them outside the intended team. <br>
Risk: Incomplete rolling GC log sets can make a partial time window look like a complete historical analysis. <br>
Mitigation: Label incomplete inputs as partial samples and update the report after collecting the full gc.log rotation set. <br>
Risk: Tuning recommendations may be misleading if log data is sparse, malformed, or not representative of the affected workload. <br>
Mitigation: Tie recommendations to observed evidence, preserve data-boundary notes, and validate changes with application owners before production rollout. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ranenwang/skills/gc-log-report) <br>
- [Publisher profile](https://clawhub.ai/user/ranenwang) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance, files] <br>
**Output Format:** [HTML report files, Markdown summaries, and concise analysis guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include embedded charts, highlighted risk items, JVM tuning rationale, and explicit notes when rolling GC logs are incomplete.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
