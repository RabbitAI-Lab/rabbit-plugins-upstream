## Description: <br>
Splits SQL files into separate object files for procedures, functions, views, triggers, tables, indexes, and constraints, then analyzes dependencies and generates dependency-ordered merge scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fish1981bimmer](https://clawhub.ai/user/fish1981bimmer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database engineers use this skill to split large SQL exports into object-level files, analyze SQL object dependencies, and convert SQL Server syntax toward Dameng-compatible SQL workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security assessment marks this release as suspicious because it includes unsafe runtime code-patching and security-evasion guidance. <br>
Mitigation: Review the scripts before installation or execution and prefer the normal split_sql_v21.py or split_sql_v22.py paths. <br>
Risk: unlimited_split.py dynamically patches and executes split_sql_v21.py at runtime. <br>
Mitigation: Avoid unlimited_split.py unless the reviewer understands and accepts the dynamic execution behavior. <br>
Risk: Generated or converted SQL may not preserve database semantics exactly. <br>
Mitigation: Keep backups of SQL inputs and review generated or converted SQL before running it against any database. <br>


## Reference(s): <br>
- [DM Converter Design](references/dm-converter-design.md) <br>
- [Split and Convert Workflow](references/split-convert-workflow-20260627.md) <br>
- [DM Converter v3.5.3 Fixes](references/dm-converter-v353-fixes.md) <br>
- [DM Converter v3.4.5 Fixes](references/dm-converter-v345-fixes.md) <br>
- [HRBI Stage Real-World Test](references/hrbi-stage-real-world-test.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/fish1981bimmer/skills/sql-splitter) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated SQL or Python script usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce split SQL files, converted SQL files, merge scripts, reports, and configuration guidance when used by an agent.] <br>

## Skill Version(s): <br>
3.6.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
