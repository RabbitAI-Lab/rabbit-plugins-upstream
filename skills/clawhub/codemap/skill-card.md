## Description: <br>
Build a compact local SQLite index of every function, class, method, interface and type across your repos, so an agent finds a symbol's file:line and signature in one lookup instead of a tree-wide grep plus whole-file read. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workloftai](https://clawhub.ai/user/workloftai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use codemap to build a local symbol index for selected repositories, then query file locations, line numbers, and signatures without repeatedly grepping and reading source files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local index can store symbol names, signatures, file paths, and line numbers from repositories the user builds over. <br>
Mitigation: Run codemap only on intended repositories, use --db to choose a controlled index location, or remove ~/.codemap/index.db when the index is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workloftai/skills/codemap) <br>
- [Workloft Labs](https://workloft.ai/labs) <br>
- [Workloft support](https://workloft.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text or JSON CLI output with file paths, line numbers, symbol kinds, and signatures.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Builds a local SQLite index at the default path ~/.codemap/index.db unless the user supplies --db.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
