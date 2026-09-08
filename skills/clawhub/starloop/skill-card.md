## Description:

Starloop reads a StarFocus todo folder and recommends up to three tractable next tasks based on star role, strategic priority, starPoints, and urgency context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[homostellaris](https://clawhub.ai/user/homostellaris)

### License/Terms of Use:

MIT-0

## Use Case:

StarFocus users and agent operators use this skill to turn a todo folder into a concise next-task recommendation, filtering by role when needed and noting high-priority tasks that are blocked by missing capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires read access to the user-provided todo folder, which may contain sensitive task details.

Mitigation: Run it only on todo folders the operator is comfortable exposing to the agent, and review folder contents before use when confidentiality matters.

Risk: For blocked high-priority todos, the skill may invoke an external `bunx clawhub search` command to look up possible capability fixes.

Mitigation: Review the proposed search term and any suggested skill before installing or running additional tools.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/homostellaris/starfocus/tree/master/agent/skills/starloop)
- [ClawHub skill page](https://clawhub.ai/homostellaris/skills/starloop)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Telegram Markdown recommendation message with full todo filenames and optional install command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns up to three ranked candidate tasks and may include blocked high-priority todos with suggested capability fixes.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
