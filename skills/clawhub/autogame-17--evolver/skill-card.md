## Description:

Evolver is a self-evolution engine for AI agents that analyzes runtime history, identifies improvements, applies protocol-constrained evolution, and communicates with EvoMap Hub through a local proxy mailbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autogame-17](https://clawhub.ai/user/autogame-17)

### License/Terms of Use:

GPL-3.0-or-later

## Use Case:

Developers and teams maintaining agent prompts, logs, and evolution assets use Evolver to generate protocol-bound GEP prompts, select reusable Genes and Capsules, and record auditable evolution events for agent improvement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install persistent hooks for multiple agent runtimes.

Mitigation: Review hook installation commands and installed files before enabling runtime integration, and remove hooks when no longer needed.

Risk: The skill can read and write local evolution state and may operate in workspaces containing sensitive files.

Mitigation: Run it in a dedicated workspace or account with only the files required for the evolution workflow.

Risk: When connected to EvoMap Hub, the validator role can run Hub-assigned validation work.

Mitigation: Set EVOLVER_VALIDATOR_ENABLED=false unless remote validation jobs are explicitly desired.

Risk: Optional network integrations can contact EvoMap and GitHub and may use a GitHub token.

Mitigation: Disable unwanted telemetry or network features and provide only narrowly scoped credentials when GitHub integration is required.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/autogame-17/skills/evolver)
- [EvoMap](https://evomap.ai)
- [EvoMap Documentation](https://evomap.ai/wiki)
- [Evolver GitHub Repository](https://github.com/EvoMap/evolver)
- [Evolver npm Package](https://www.npmjs.com/package/@evomap/evolver)
- [From Procedural Skills to Strategy Genes](https://arxiv.org/abs/2604.15097)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown/text guidance with shell command snippets and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce GEP prompts, evolution events, local memory updates, hook configuration, and validation reports depending on CLI mode and host integration.]

## Skill Version(s):

1.91.0 (source: package.json and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
