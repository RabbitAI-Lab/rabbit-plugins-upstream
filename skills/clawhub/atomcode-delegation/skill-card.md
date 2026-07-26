## Description: <br>
Delegates independent coding tasks to the AtomCode CLI in headless mode, with patterns for single-task runs, parallel batches, monitoring, timeouts, and session resume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentlau2046-sudo](https://clawhub.ai/user/vincentlau2046-sudo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to hand off scoped code-editing tasks to AtomCode from an agent session, including batch runs that need PID tracking, timeouts, logging, and result review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-approved background agents can make unintended code edits or run longer than expected. <br>
Mitigation: Use a clean branch or separate worktree, verify the AtomCode workdir, set max-turns and a timeout, and review git status and diffs before accepting changes. <br>
Risk: Parallel AtomCode runs in the same workspace can conflict or produce partial results. <br>
Mitigation: Run independent tasks in isolated worktrees when possible, keep concurrency conservative, track PIDs and logs, and verify completion markers plus diffs. <br>


## Reference(s): <br>
- [AtomCode CLI](https://atomgit.com/atomcode) <br>
- [ClawHub Skill Page](https://clawhub.ai/vincentlau2046-sudo/skills/atomcode-delegation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and task templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts and command examples should be adapted to the target workdir, provider, max-turns limit, and review workflow.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
