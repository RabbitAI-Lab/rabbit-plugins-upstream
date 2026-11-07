## Description:

A Minecraft toolkit for finding and managing mods, analyzing crashes and compatibility, translating resources, migrating versions, and syncing saves.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

Minecraft players and modpack authors can use the toolkit to inspect mod files, find compatible mods, troubleshoot crashes, translate resources, assess migrations, and back up or restore saves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags activity reporting despite offline settings, suppressed safety explanations, and insufficient limits on file changes.

Mitigation: Postpone installation until reporting is controlled, offline mode blocks every request, safety explanations remain available, and file destinations are constrained. Evaluate with isolated save and mod copies, keep synchronized configuration private, and block unwanted network access independently. Do not send license details over HTTP.

Risk: Server delivery, data retention, and authorization enforcement were not verified because the server implementation is absent.

Mitigation: Keep network access blocked unless required and independently review server behavior before providing license details or enabling reporting.

## Reference(s):

- [ClawHub release](https://clawhub.ai/liang030214/skills/scan-probe-legacy)
- [Publisher profile](https://clawhub.ai/user/liang030214)
- [Publisher homepage](https://github.com/Liang030214/mc-skill-v1)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON, HTML files, Shell commands, Configuration instructions]

**Output Format:** [JSON results and HTML reports, with guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the requested Minecraft task and supplied files.]

## Skill Version(s):

0.0.1 (source: target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
