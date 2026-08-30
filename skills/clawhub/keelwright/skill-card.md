## Description:

Keelwright Fix helps AI coding agents run supervised loop-coding sessions with machine-enforced safety checks, autonomy controls, self-learning records, web prompt-injection guards, and plain-language reports for users who cannot review every line of generated code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and product builders use this skill to supervise AI-generated coding work, especially autonomous or loop-based sessions where security gates, stop conditions, and plain-language status reports are needed. It is intended for coding workflows where users want the agent to check risky changes, produce evidence, and pause for approval on sensitive areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad operational authority over files, shell commands, network checks, git actions, browser-related checks, and persistent local records.

Mitigation: Install only when this supervision role is desired, start in Checkpoint or Copilot mode for sensitive work, and review proposed commands and file changes before allowing autonomous execution.

Risk: Persistent learning and logging can create or update PROGRESS.md, autoresearch-lessons.md, phoenix-log.md, and home-directory Keelwright logs that may contain project context.

Mitigation: Decline or disable bootstrap and logging features when persistence is not wanted, keep generated records out of commits, and review those files before sharing a repository.

Risk: Autonomous coding sessions can affect sensitive areas such as authentication, payments, databases, production deploys, deletes, or public posting.

Mitigation: Use Checkpoint or Copilot mode for these areas so the agent pauses for human approval before acting.

Risk: Update checks, weekly self-improvement, attack logging, and promotional prompts may perform behavior users do not expect from passive documentation.

Mitigation: Disable or decline those features unless they are wanted, and confirm network and logging behavior before using the skill in private or regulated projects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Architecture reference](assets/architecture.md)
- [QA results and methodology](qa-results/README.md)
- [Security gates](references/security-gates.md)
- [Web guard](references/web-guard.md)
- [Remediation guide](references/remediation.md)
- [Provenance notes](references/provenance.md)
- [GitHub security workflow](https://github.com/ratingtesting/keelwright/actions/workflows/security.yml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, file paths, reports, and optional generated project-tracking files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for user approval before bootstrap or sensitive actions; can direct agents to run local scripts and create or update local tracking files when enabled.]

## Skill Version(s):

1.9.1 (source: server release metadata; artifact frontmatter says 1.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
