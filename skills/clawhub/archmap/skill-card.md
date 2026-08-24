## Description:

ArchMap is a terminal-native architecture mapping agent that analyzes local project source, builds architecture baselines, and produces incremental impact, sync, and diff reports for development planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xu-jin-cs](https://clawhub.ai/user/xu-jin-cs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use ArchMap to scan a local codebase, generate architecture and dependency reports, and identify affected modules, files, APIs, storage, and tests for a requested change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local project source and writes analysis artifacts into the target project's archmap directory.

Mitigation: Run it only against intended project paths and review generated artifacts before sharing them outside the project team.

Risk: Dependency and optional local-tool integrations can change the trust boundary of the run.

Mitigation: Use a pinned or controlled Python environment, and enable documented expert-router, gate-switch, or retro-skill-dispatcher integrations only when those local tools are present and trusted.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/xu-jin-cs/dsh-skills/tree/main/archmap)
- [ClawHub skill page](https://clawhub.ai/xu-jin-cs/skills/archmap)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown, JSON, JSONL, and Mermaid text files written under the target project's archmap directory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local project source and writes text analysis artifacts; does not generate images or start a web service.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
