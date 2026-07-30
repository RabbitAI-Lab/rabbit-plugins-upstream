## Description: <br>
Rune is a 66-skill mesh for AI coding assistants that routes software work across planning, implementation, review, deployment, memory, and domain extension workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhadaututtheky](https://clawhub.ai/user/nhadaututtheky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use Rune as an opinionated automation layer for coding tasks, including code changes, audits, debugging, deployment workflows, documentation, persistent project context, and domain-specific extension packs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rune is a broad automation layer with routing authority across many coding workflows. <br>
Mitigation: Review enabled workflows before installation and keep human approval gates for code changes, shell commands, deployment, and external service actions. <br>
Risk: Persistent memory and project-state features can capture or load project context across sessions. <br>
Mitigation: Review or disable automatic Neural Memory capture and inspect .rune files before loading or sharing project state. <br>
Risk: Deployment and launch workflows may interact with production systems when credentials and platform tools are available. <br>
Mitigation: Do not provide production, cloud, GitHub, Zalo, or messaging credentials until the desired workflow and approval gates are confirmed. <br>
Risk: Onboarding and session workflows can write CLAUDE.md and .rune files into a project. <br>
Mitigation: Run the skill in a clean branch or reviewed workspace and inspect generated context files before committing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nhadaututtheky/skills/rune-kit) <br>
- [Rune Documentation](https://rune-kit.github.io/rune) <br>
- [Rune Guides](https://rune-kit.github.io/rune/guides) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions, reports, command suggestions, code edits, configuration files, and generated project context files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write CLAUDE.md and .rune state files, route work across bundled skill documents, and propose or execute shell commands when the host agent grants tool access.] <br>

## Skill Version(s): <br>
2.30.3 (source: server release metadata, created 2026-07-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
