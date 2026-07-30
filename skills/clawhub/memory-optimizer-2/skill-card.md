## Description: <br>
Analyzes AI agent memory files to detect duplicates, stale information, missing indexes, and structure issues, then generates reports and optional cleanup recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lokix94](https://clawhub.ai/user/lokix94) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to audit AI agent memory markdown files for duplication, stale context, missing indexes, and structural issues. It can produce an analysis report and, when explicitly applied, perform common cleanup actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Applied optimizations can remove, archive, or reorganize memory context that may still be useful. <br>
Mitigation: Run the analyzer and dry-run output first, review proposed changes, and use the backup option before applying modifications. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lokix94/skills/memory-optimizer-2) <br>
- [Server-resolved GitHub provenance](https://github.com/lokix94/peru-hub/tree/main/skills/memory-optimizer) <br>
- [Publisher profile](https://clawhub.ai/user/lokix94) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, optional JSON analysis output, and shell command instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optimization changes require an explicit apply command; backups are available when applying changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
