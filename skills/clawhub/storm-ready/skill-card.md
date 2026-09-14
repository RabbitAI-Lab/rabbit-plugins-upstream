## Description:

Storm Ready helps agents produce household severe-weather preparedness audits, supply-sizing guidance, and phase-by-phase checklists for regional hazards such as hurricanes, tornadoes, ice storms, wildfires, atmospheric rivers, and blizzards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to plan household storm readiness before severe weather, audit emergency-kit gaps, size water, food, and backup power, and generate countdown checklists. It is preparedness guidance only and does not replace official alerts, evacuation orders, or emergency services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat preparedness guidance as a substitute for official weather alerts, evacuation orders, or emergency services.

Mitigation: Use the skill only to organize preparation; follow national weather service and local emergency-management instructions and call emergency services during active life-threatening events.

Risk: The tool can store household preparedness details locally in ~/.storm-ready.json unless a custom --file path is provided.

Mitigation: Use --file for an explicit storage location, protect or delete the local profile as appropriate, and avoid storing sensitive details on shared systems.

## Reference(s):

- [Region Playbooks](references/region-playbooks.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/storm-ready)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/storm-ready)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or read a local household profile at ~/.storm-ready.json unless a --file path is supplied.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
