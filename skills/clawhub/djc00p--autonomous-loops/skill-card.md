## Description: <br>
Autonomous agent loop patterns: sequential pipelines, persistent REPL sessions, parallel spec-driven generation, PR automation, cleanup passes, and RFC-driven DAG orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[djc00p](https://clawhub.ai/user/djc00p) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to choose and apply autonomous agent loop patterns for iterative coding workflows, PR automation, parallel generation, cleanup passes, and DAG-based feature work. It is intended for repositories where the user can enforce consent, dry-run execution, branch protections, least-privileged credentials, and human merge approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact repository automation may create branches, open pull requests, retry CI, or merge code with inconsistent safeguards around writes and auto-merge. <br>
Mitigation: Use dry-run first execution, protected branches, least-privileged GitHub credentials, hard cost/time/run limits, and explicit human approval before every merge. <br>
Risk: Session files, shared notes, diffs, specs, and CI logs can expose secrets, customer data, internal paths, or proprietary code structure. <br>
Mitigation: Redact sensitive content before passing it to agents, gitignore session and loop files, restrict file permissions, and treat logs and shared notes as sensitive artifacts. <br>
Risk: Parallel or DAG-based agents can overwrite each other, write outside intended paths, or amplify conflicts if work is not isolated. <br>
Mitigation: Run agents in isolated worktrees or per-run directories, validate output paths, minimize file overlap, and route merge conflicts to a human instead of automatic retries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/djc00p/skills/autonomous-loops) <br>
- [Publisher Profile](https://clawhub.ai/user/djc00p) <br>
- [Security Checklist](references/security-checklist.md) <br>
- [Sequential Pipeline](references/sequential-pipeline.md) <br>
- [Persistent REPL](references/persistent-repl.md) <br>
- [Parallel Agents](references/parallel-agents.md) <br>
- [PR Automation Loop](references/pr-automation.md) <br>
- [De-Sloppify Pattern](references/de-sloppify.md) <br>
- [DAG Orchestration](references/dag-orchestration.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command examples, checklists, code snippets, and configuration flags] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires gh, git, and node; uses CLAW_SESSION and CLAW_SKILLS when running session-based examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
