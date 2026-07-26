## Description: <br>
Resolve dependency or version conflicts across npm, pip, yarn, pnpm, Maven, and Go modules by explaining the conflict, ranking resolution options, and providing exact commands with verification steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to diagnose dependency installation failures, understand incompatible version constraints, and choose a ranked fix with commands, manifest edits, and verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proposed dependency commands or manifest edits can change application install behavior or mask a conflict if applied without review. <br>
Mitigation: Review each proposed command or edit before applying it, prefer the ranked safer options, and run the included verification steps after the fix. <br>
Risk: Force-style dependency options can bypass dependency resolution instead of correcting the underlying incompatibility. <br>
Mitigation: Use force-style options only as a last resort and document why safer alignment, upgrade, or override options were not sufficient. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/mohitagw15856/skills/dependency-conflict-resolver) <br>
- [Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/dependency-conflict-resolver.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Ranks resolution options by safety and includes verification and prevention guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
