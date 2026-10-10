## Description:

Install a durable Challenge the Direction rule into an agent's AGENTS.md after explicit user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[srmhrrm-hub](https://clawhub.ai/user/srmhrrm-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add a durable decision-quality rule to a workspace AGENTS.md so the agent challenges weak premises before consequential work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent instruction change can alter agent behavior in the wrong workspace if the target AGENTS.md is misidentified.

Mitigation: Show the exact target path before editing, require explicit user approval, and report that the rule applies only where that AGENTS.md is loaded.

Risk: Repeated installation attempts could duplicate or conflict with existing decision-quality instructions.

Mitigation: Check for an equivalent section first, preserve unrelated instructions, and re-read the file to verify the rule appears exactly once.

## Reference(s):

- [Critical Thinking on ClawHub](https://clawhub.ai/srmhrrm-hub/skills/critical-thinking)
- [srmhrrm-hub Publisher Profile](https://clawhub.ai/user/srmhrrm-hub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown instructions and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit the active workspace AGENTS.md only after explicit user approval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
