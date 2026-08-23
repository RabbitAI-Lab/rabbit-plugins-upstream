## Description:

Guides agents through safe Go refactoring using coverage-adaptive safety checks, tool-driven behavior-preserving changes, staged human-reviewed PRs, and Go-specific structural patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to plan, execute, and review behavior-preserving Go refactors such as renames, extractions, package moves, import-cycle breaks, and staged modernization work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Go code, run Go and Git tooling, create branches or worktrees, and potentially open GitHub PRs after approval.

Mitigation: Review the refactoring inventory, approval prompts, and verification plan before authorizing changes or PR creation.

Risk: Untested code, exported API changes, deletions, and package moves can be expensive to reverse if a refactor is sequenced poorly.

Mitigation: Require the skill's human checkpoints, add characterization tests for weakly covered code, and keep each step behavior-preserving and separately verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/golang-refactoring)
- [Project homepage from metadata](https://github.com/samber/cc-skills-golang)
- [Workflow reference](references/workflow.md)
- [Safety net reference](references/safety-net.md)
- [Go tooling reference](references/go-tooling.md)
- [Structural refactoring reference](references/structural.md)
- [Refactoring catalog](references/catalog.md)
- [Go issue tracker](https://github.com/golang/go/issues)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline Go, shell, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include refactoring inventories, approval checkpoints, verification command plans, code edits, branch or PR steps, and review findings.]

## Skill Version(s):

1.1.0 (source: SKILL.md metadata.version and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
