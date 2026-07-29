## Description: <br>
Keelwright helps AI coding agents run autonomous coding loops with machine-enforced security gates, autonomy controls, circuit breakers, and plain-language reports for users who cannot review every code change line by line. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ratingtesting](https://clawhub.ai/user/ratingtesting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Vibe-coders, loop-coders, non-developer founders, and product builders use Keelwright to put guardrails around AI-generated code during coding sessions, autonomous runs, and commits. It guides agents to run security checks, control autonomy, stop runaway loops, and report results in plain language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs agents to automatically change project files and maintain persistent project-root state. <br>
Mitigation: Review before installing and use a disposable branch, worktree, or sandbox unless automatic project-root files are acceptable; disable or edit the first-load bootstrap when explicit approval is required. <br>
Risk: The skill can guide agents to install tools, run scanners, download browser assets, orchestrate subagents, and commit code during unattended work. <br>
Mitigation: Use Checkpoint or Copilot mode for sensitive repositories, require approval for installs and commits, and avoid no-confirm Autopilot behavior unless the environment is disposable. <br>
Risk: Self-learning and unattended improvement behaviors can change repository state in ways the user may not expect. <br>
Mitigation: Turn off weekly self-improvement and persistent learning files when repository changes must be explicitly controlled, and audit generated files and diffs before merging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright) <br>
- [Publisher profile](https://clawhub.ai/user/ratingtesting) <br>
- [Author profile from clawdis metadata](https://github.com/ratingtesting) <br>
- [README](README.md) <br>
- [Security gates](references/security-gates.md) <br>
- [Circuit breaker](references/circuit-breaker.md) <br>
- [QA testing methodology](references/qa-testing.md) <br>
- [QA results](qa-results/README.md) <br>
- [Provenance notes](references/provenance.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code examples, configuration snippets, and plain-language status reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to produce on-disk evidence, concise gate outcomes, autonomy decisions, and final summaries.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
