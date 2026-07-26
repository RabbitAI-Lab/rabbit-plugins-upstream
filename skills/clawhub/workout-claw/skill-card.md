## Description: <br>
Log workouts, track progress, compute PRs, edit/delete sessions via a local CLI. Local-first, JSON storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dsdevq](https://clawhub.ai/user/dsdevq) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
People who track gym training can have an agent log sessions, query workout history, compute estimated PRs, review muscle-group volume, and manage local workout records through the workout-claw CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The required global npm CLI can create, edit, and delete local workout log files. <br>
Mitigation: Install a pinned CLI version such as workout-claw@0.3.1 and review commands before execution. <br>
Risk: Delete operations are non-interactive and can remove local workout sessions without a CLI confirmation prompt. <br>
Mitigation: Show the exact session ID to the user and require explicit confirmation before invoking delete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dsdevq/skills/workout-claw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; CLI commands return YAML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the workout-claw binary on PATH and stores workout logs as local JSON files under ~/.workout-claw/.] <br>

## Skill Version(s): <br>
0.3.1 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
