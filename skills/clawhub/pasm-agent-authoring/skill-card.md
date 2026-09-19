## Description:

PASM Agent Authoring Kit helps developers build PASM agents with a BaseAgent SDK, scenario and contract-check tooling, and skill packaging utilities that run offline with no LLM dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create PASM-based agents, package them for platform release, and run validation-style checks for agent behavior. It is suited to agent authoring workflows that need offline operation, local state persistence, and explicit engine-tier reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs users to install and run the pasm-skills package, while the submitted artifact contains documentation rather than the package implementation.

Mitigation: Install in an isolated virtual environment, pin pasm-skills to a trusted version, and review the package source before using it in higher-assurance workflows.

Risk: Agents built from the kit can persist local state under ~/.pasm-agents, including persona, interaction, feedback, mood, notes, and memory data.

Mitigation: Review what data agents save, avoid storing sensitive information unless appropriate for the use case, and clear the relevant ~/.pasm-agents entries when state retention is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-agent-authoring)
- [Project homepage](https://github.com/arronJack/pasm-skills)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include package installation steps, agent subclass examples, packaging commands, and guidance for local state stored under ~/.pasm-agents.]

## Skill Version(s):

0.5.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
