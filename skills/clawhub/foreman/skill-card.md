## Description:

Foreman helps an agent dispatch coding tasks to background worker agents, isolate each task in a git worktree, and run intake and acceptance checks before merging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use Foreman to batch implementation work to configured worker backends or to review delivered code while preserving task state, path boundaries, and verification gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository code may be sent to configured worker backends.

Mitigation: Use the skill only with worker backends you trust for the repository content, and review handoff-cli provenance before installing or upgrading it.

Risk: The optional caged worker passes DEEPSEEK_API_KEY into a container whose network is not restricted.

Mitigation: Use a dedicated low-limit key, rotate it regularly, and add a network allowlist or proxy when credential exposure would matter.

Risk: Autonomous workers may make unwanted repository changes if they run in the main checkout.

Mitigation: Keep workers pointed at task git worktrees, enforce allowed-path checks, and inspect generated .foreman state before merging.

Risk: CI gate changes can affect whether delivered work is accepted.

Mitigation: Inspect generated CI workflow changes before merging and preserve the rule that builders must not edit tests, assertions, or CI configuration used to judge their work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/foreman)
- [Dispatch workflow](artifact/dispatch.md)
- [Acceptance workflow](artifact/verify.md)
- [Work order template](artifact/work-order.md)
- [DeepSeek balance endpoint](https://api.deepseek.com/user/balance)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON state shapes, workflow templates, and helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate work orders, task state, git worktree commands, CI gate configuration, and acceptance instructions.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
