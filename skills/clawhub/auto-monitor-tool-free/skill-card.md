## Description: <br>
Auto Monitor Tool Free helps an agent check single-machine CPU, memory, disk, network, process, and basic service status, with simple threshold alerts and local history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and personal server owners use this skill to inspect local system health, view top resource-consuming processes, configure basic thresholds, and receive simple console or email alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SMTP or callback notifications can disclose host details outside the monitored machine. <br>
Mitigation: Review notification destinations and credentials before use, and send alerts only to approved endpoints. <br>
Risk: Local monitoring commands can expose system status, process, disk, network, and history information. <br>
Mitigation: Run the skill only on machines where the user is authorized to inspect those details, and keep requests scoped to explicit monitoring tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/auto-monitor-tool-free) <br>
- [Project homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with command examples and structured status, alert, log, and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local system metrics, alert status, process summaries, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
