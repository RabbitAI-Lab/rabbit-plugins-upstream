## Description: <br>
Convert Unix timestamps and date strings between formats, parse dates, handle timezones, calculate differences, and add seconds with timezone support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run a local Python CLI for converting Unix timestamps, parsing date strings, formatting dates in different timezones, and calculating time differences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exact date math may be misleading if timezone, input format, or relative-date assumptions are ambiguous. <br>
Mitigation: Use explicit timezones and input formats for critical conversions, and verify important results against expected boundary cases. <br>
Risk: The skill may activate for broad date parsing or timezone-formatting questions. <br>
Mitigation: Use it for timestamp and date conversion tasks, and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fuzzyb33s/skills/timestamp-converter) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text command output and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local Python standard library CLI; security evidence found no hidden access, persistence, network use, credential handling, or destructive behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
