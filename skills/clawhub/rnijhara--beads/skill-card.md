## Description: <br>
Beads Task Tracker helps AI agents use the bd CLI to manage git-backed tasks, dependencies, ready work queues, and multi-step project state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rnijhara](https://clawhub.ai/user/rnijhara) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate issue tracking, dependency management, ready-task selection, task updates, and handoff state through Beads in a repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to initialize and update Beads state in a repository, which can write .beads/ data. <br>
Mitigation: Review repository state changes before accepting them, and restrict bd init or task update commands in repositories where agent-managed task state is not desired. <br>
Risk: The skill documents bd hooks install and bd init behavior that can install Git hooks. <br>
Mitigation: Review or disable hook installation in environments that require controlled Git hook policy. <br>
Risk: The skill recommends bd sync, which can commit changes and push task contents to configured remotes. <br>
Mitigation: Run sync only against approved remotes and review task content before pushing from sensitive repositories. <br>


## Reference(s): <br>
- [Beads Task Tracker on ClawHub](https://clawhub.ai/rnijhara/skills/beads) <br>
- [rnijhara publisher profile](https://clawhub.ai/user/rnijhara) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON-oriented command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the bd CLI; command examples favor --json for machine-readable output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
