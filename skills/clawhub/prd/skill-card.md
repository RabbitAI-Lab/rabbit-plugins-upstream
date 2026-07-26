## Description: <br>
Create and manage Product Requirements Documents (PRDs) for structured feature planning with user stories, acceptance criteria, and implementation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, product managers, and coding-agent operators use this skill to create AI-ready PRDs with small user stories, verifiable acceptance criteria, dependency ordering, and progress tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents unattended coding-agent execution with permission bypass and repository commits. <br>
Mitigation: Use human review, an isolated worktree, and explicit approval before commits unless unattended automation is intentionally accepted. <br>
Risk: PRDs can drive broad automated code changes when stories are too large or acceptance criteria are vague. <br>
Mitigation: Keep stories small, dependency ordered, and verifiable; review the PRD before using it to execute implementation work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bjesuiter/skills/prd) <br>
- [Agent Usage Patterns](artifact/references/agent-usage.md) <br>
- [Output Patterns and Templates](artifact/references/output-patterns.md) <br>
- [Workflow Patterns for PRD Skills](artifact/references/workflows.md) <br>
- [Ralph by snarktank](https://github.com/snarktank/ralph) <br>
- [Claude Code](https://github.com/anthropics/claude-code) <br>
- [Amp Code](https://ampcode.com) <br>
- [Tips for AI Coding with Ralph Wiggum](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON templates with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create or update prd.json, prompt.md, and progress.txt.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
