## Description:

Gmira guides agents through building, redesigning, and reviewing web surfaces with deliberate visual direction, registry component repair, canvas and WebGL craft, accessibility, performance, and multi-viewport verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Gmira to build or repair websites, e-commerce flows, dashboards, portfolios, marketing pages, and similar web surfaces that need a committed visual direction instead of generic generated layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may edit project UI code, add dependencies, and install registry components.

Mitigation: Review dependency changes, generated code, and copied registry components before shipping.

Risk: The skill applies an opinionated house style that may conflict with brand, accessibility, legal, or user requirements.

Mitigation: Override the style guidance when project requirements demand a different voice, visual system, accessibility treatment, or legal wording.

Risk: Visual verification guidance can miss issues if screenshots and runtime behavior are not actually inspected.

Mitigation: Run the recommended viewport checks and inspect rendered screenshots before handoff or release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/gmira)
- [Server-resolved GitHub provenance](https://github.com/OthmanAdi/gmira/tree/main/skills/gmira)
- [Gmira doctrine](references/DOCTRINE.md)
- [Canvas craft rules](references/canvas-craft-rules.md)
- [Canvas primitives](references/canvas-primitives.md)
- [Registry component finding](references/finding-01-tame-the-arsenal.md)
- [Idle state finding](references/finding-02-idle-state.md)
- [Material worlds playbook](references/playbooks/worlds.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose UI edits, dependency additions, registry component repairs, and visual verification steps.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
