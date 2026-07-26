## Description: <br>
Audits Chinese novel manuscripts for logic flaws, character inconsistency, pacing problems, and narrative bugs, then returns graded reports and repair suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbroot](https://clawhub.ai/user/bbroot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authors, editors, and writing assistants use this skill to review Chinese novel chapters or full manuscripts for plot logic, character consistency, pacing, foreshadowing, and repair priorities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect private manuscripts or novel-master workspace files. <br>
Mitigation: Run it only on explicit manuscript files or book paths that the user intends to review. <br>
Risk: The v2 workflow can call cross-skill novel-master commands against local book state. <br>
Mitigation: Use v2 cross-skill commands only when the installed novel-master skill and target book path are trusted. <br>
Risk: Generated reports can contain manuscript details or analysis that should not be shared broadly. <br>
Mitigation: Check report, log, and visualization output locations before sharing or publishing results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bbroot/skills/novel-bug-checker) <br>
- [README](README.md) <br>
- [English README](README_EN.md) <br>
- [Bug Patterns](references/bug-patterns.md) <br>
- [Character Consistency](references/character-consistency.md) <br>
- [Narrative Theory](references/narrative-theory.md) <br>
- [Repair Strategies](references/repair-strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports with optional inline shell commands and saved report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read explicit manuscript files and produce local analysis reports when the user requests script-based checks.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
