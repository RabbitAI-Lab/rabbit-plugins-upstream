## Description:

Create and run a text-only pet adventure diary driven by real-world locations, local time, weather, D20-style event checks, and emergency phone calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jichengkai](https://clawhub.ai/user/jichengkai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and operate a Chinese text-only traveling pet diary in a chosen workspace, advance daily journeys, review status, and resolve D20-style phone-call events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and updates persistent pet-life/ files in the selected workspace.

Mitigation: Run it only in an intended workspace, review the generated pet-life/ folder, and avoid using sensitive directories for the simulation state.

Risk: Daily advance can contact Open-Meteo for weather for the pet's in-game location.

Mitigation: Use the documented --offline option when network access is not desired.

Risk: Unanswered urgent phone-call events may be auto-resolved and change the simulated diary state.

Mitigation: Check status before advancing the diary and answer pending calls before their deadlines when user choice matters.

## Reference(s):

- [宠物冒险生活规则](references/rules.md)
- [OpenClaw Integration](references/openclaw.md)
- [ClawHub Skill Page](https://clawhub.ai/jichengkai/skills/pet-adventure-life)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown diary entries, JSON command results, and concise Chinese user-facing guidance with shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates pet-life/ state, world, event, call, and diary files in the selected workspace.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
