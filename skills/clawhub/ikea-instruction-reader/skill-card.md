## Description:

Guides agents through flat-pack furniture assembly by decoding diagram-only instructions, tracking parts and progress, producing tool checklists, identifying likely steps from photos, and warning about common mistakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to turn diagram-only flat-pack furniture manuals into practical assembly guidance, parts tracking, tool checklists, and mistake warnings. It is intended for furniture assembly tasks where the user needs help interpreting printed or visual instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assembly tracker can create and update local progress state in the user's home directory.

Mitigation: Tell users before running the tracker script; users who do not want local state can avoid the tracker or remove ~/.assembly_tracker afterward.

Risk: Furniture assembly guidance may be generic and may not match a specific manufacturer's exact manual or safety requirements.

Mitigation: Use the skill as guidance alongside the official manual, verify part orientation and quantities before tightening hardware, and follow manufacturer safety steps such as wall anchoring.

## Reference(s):

- [Furniture Assembly Reference](references/hardware_guide.md)
- [Server-resolved source repository](https://github.com/voronindenis5/ikea-instruction-reader)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/ikea-instruction-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and terminal-style text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a local assembly progress file when the tracker script is run.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
