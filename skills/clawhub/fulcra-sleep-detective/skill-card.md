## Description: <br>
Retired Fulcra sleep-analysis skill. Route new work to fulcra-context and keep all sleep, biometric, calendar, and location reads explicit, bounded, and user-approved. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agents use this retired routing package to redirect sleep, biometric, calendar, and location workflows to current Fulcra skills while preserving explicit consent and bounded data access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill concerns sensitive sleep, biometric, calendar, and location context. <br>
Mitigation: Require current-request consent, read the smallest useful time window and metric set, and prefer summaries or aggregates over raw records. <br>
Risk: Operational workflows may involve credentials, API access, or write capabilities. <br>
Mitigation: Install only for intended Fulcra workflows, verify token scope before high-impact use, and keep confirmation and dry-run steps in place. <br>
Risk: Retired commands or autonomous monitoring patterns could reintroduce unnecessary collection or retention. <br>
Mitigation: Do not invoke retired commands, background polling, proactive alerts, exports, screenshots, or durable storage unless the user explicitly approves that exact workflow. <br>


## Reference(s): <br>
- [Fulcra Platform](https://fulcradynamics.com) <br>
- [Fulcra Developer Docs](https://fulcradynamics.github.io/developer-docs/) <br>
- [Current Context Skill](https://clawhub.ai/arc-claw-bot/skills/fulcra-context) <br>
- [Annotation Skill](https://clawhub.ai/arc-claw-bot/skills/fulcra-annotations) <br>
- [Skill Page](https://clawhub.ai/arc-claw-bot/skills/fulcra-sleep-detective) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and routing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill provides guidance only; it does not ship the retired sleep-analysis scripts.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
