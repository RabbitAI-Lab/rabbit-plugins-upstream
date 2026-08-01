## Description: <br>
Enforces fresh verification evidence before any completion claim, including claims that tests pass, a bug is fixed, work is done, a branch is ready to merge, or ambiguous-scope work is ready to begin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to choose and run appropriate verification before making completion, merge-readiness, build, test, or bug-fix claims. It also helps confirm task scope before broad edits and requires explicit evidence when verification fails or is limited. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to run real verification commands and inspect or modify repository state. <br>
Mitigation: Review proposed commands and git operations before execution, especially stashing, committing, temporary worktree creation, and cleanup. <br>
Risk: A broad or ambiguous task can expand across multiple subsystems before the user has confirmed the intended scope. <br>
Mitigation: Use the pre-edit scope confirmation gate and blast-radius summary before making edits. <br>
Risk: Local verification can be misleading when unrelated work-in-progress is present. <br>
Mitigation: Use isolated verification for high-impact changes or dirty working trees, applying only the owned diff to a clean base before claiming success. <br>


## Reference(s): <br>
- [Isolated Verification](artifact/references/isolated-verification.md) <br>
- [System-Wide Test Check](artifact/references/system-wide-test-check.md) <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion) <br>
- [Publisher profile](https://clawhub.ai/user/iliaal) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured completion reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the agent to produce fresh verification evidence and to report limits, failures, and scope decisions explicitly.] <br>

## Skill Version(s): <br>
4.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
