## Description:

Build or review frontend UI for clean, restrained, human-designed interfaces without generic AI visual patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill as a visual-quality guardrail when building, revising, or reviewing frontend interfaces with AI coding agents. It helps keep generated UI practical, scannable, and aligned with existing product requirements and design systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer UI decisions strongly enough to conflict with product requirements, accessibility, localization, security, data correctness, or an existing design system.

Mitigation: Keep those requirements authoritative, apply the skill as a visual-quality guardrail, and document any justified exception when a no-slop rule conflicts.

Risk: The checklist may reject valid domain-specific branding, motion, or visual treatment if applied without context.

Mitigation: Use the review checklist as an acceptance aid, not a substitute for domain judgment, and escalate rather than revise when a visual rule conflicts with the product need.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/leostehlik/skills/no-slop-ui)
- [SKILL.md](SKILL.md)
- [Banned UI Patterns](references/banned-patterns.md)
- [Colour Palettes](references/colour-palettes.md)
- [Agent Snippets](docs/agent-snippets.md)
- [No Slop UI v0.3 Conversion Proof](docs/conversion-proof.md)
- [No Slop UI Review Checklist](examples/review-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code, shell command snippets, and checklist verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Framework-agnostic frontend guidance; no hidden data access, persistence, or unsafe execution behavior found in ClawHub security evidence.]

## Skill Version(s):

0.3.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
