## Description:

Decode, track, and guide through furniture assembly instructions from step diagrams by managing parts inventory, tracking progress, identifying current steps from photos, and warning about common mistakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users assembling flat-pack furniture use this skill to translate diagram-only assembly steps into plain-language guidance, track parts and progress, prepare tools, and surface common safety or assembly mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The assembly tracker creates or updates a local progress file under the user's home directory.

Mitigation: Use it for non-sensitive assembly projects and review the local progress state before sharing logs or support transcripts.

Risk: Some README command examples may not match the script's supported arguments.

Mitigation: Rely on the script help output when a command fails.

Risk: Assembly guidance can affect furniture stability and safety if applied to the wrong product or step.

Mitigation: Cross-check guidance against the official product manual and follow wall-anchor or anti-tip instructions for tall furniture.

## Reference(s):

- [Furniture Assembly Reference](references/hardware_guide.md)
- [Server-resolved source repository](https://github.com/voronindenis5/ikea-instruction-reader)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/ikea-instruction-reader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a local progress file under the user's home directory when the assembly tracker script is used.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
