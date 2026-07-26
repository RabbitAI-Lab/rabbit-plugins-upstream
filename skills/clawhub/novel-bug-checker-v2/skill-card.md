## Description: <br>
Audits Chinese novel manuscripts for logic flaws, character inconsistency, pacing issues, and narrative bugs, then produces graded reports and repair suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbroot](https://clawhub.ai/user/bbroot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and developers use this skill to audit Chinese novel chapters or manuscripts for logic flaws, character consistency problems, pacing issues, foreshadowing gaps, and prioritized repair options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled templates and examples include host diagnostics and publishing-style actions beyond ordinary narrative review. <br>
Mitigation: Review templates before use and treat diagnostics, publishing, and reader-notification content as out of scope unless separately authorized. <br>
Risk: The optional novel-master integration can execute cross-skill commands against local project state. <br>
Mitigation: Authorize novel-master integration explicitly and run it only against intended local manuscript workspaces. <br>
Risk: The skill may create local reports or logs during analysis. <br>
Mitigation: Run it in an appropriate workspace and inspect generated report or log files before sharing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bbroot/skills/novel-bug-checker-v2) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Bug patterns reference](artifact/references/bug-patterns.md) <br>
- [Character consistency reference](artifact/references/character-consistency.md) <br>
- [Narrative theory reference](artifact/references/narrative-theory.md) <br>
- [Repair strategies reference](artifact/references/repair-strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports with optional plain-text templates and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run local Python analyzers and produce local report or log files; optional novel-master integration should be explicitly authorized.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
