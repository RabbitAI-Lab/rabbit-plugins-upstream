## Description:

Guides coding agents and developers in deciding whether an agent constraint belongs in hooks, permissions, AGENTS.md or CLAUDE.md, skills, path-scoped rules, or a one-off prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to govern coding-agent behavior constraints, choose the lowest reliable enforcement layer, and avoid overloading persistent agent instruction files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation makes the guidance available in every Claude Code project.

Mitigation: Install project-locally unless the user intentionally wants the skill available across all projects.

Risk: The optional SessionEnd hook can keep a local log of session IDs, working directories, end reasons, and transcript paths.

Mitigation: Enable the hook only after reviewing the logging behavior and confirming that local retention of this metadata is acceptable.

Risk: Constraint governance recommendations can affect hooks, permissions, memory-derived recommendations, or agent instruction files.

Mitigation: Review proposed settings, hook, permission, and instruction changes before applying them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/snowsonz/skills/agent-constraints)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Evidence](artifact/EVIDENCE.md)
- [Layer 1 Enforcement](artifact/LAYER1-ENFORCEMENT.md)
- [Layer 2 Instructions](artifact/LAYER2-INSTRUCTIONS.md)
- [Layer 3 On-Demand](artifact/LAYER3-ONDEMAND.md)
- [Hooks README](artifact/hooks/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to agent instruction files, hooks, permissions, skills, or path-scoped rules for human review.]

## Skill Version(s):

0.1.4 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
