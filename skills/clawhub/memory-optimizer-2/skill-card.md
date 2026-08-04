## Description: <br>
Analyzes AI agent memory files to detect duplicates, stale information, missing indexes, and structural issues, generating reports and optional cleanup actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lokix94](https://clawhub.ai/user/lokix94) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to inspect local AI agent memory markdown files, generate memory health reports, and optionally apply deduplication, re-indexing, stale-entry cleanup, and structure fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Applying optimizations can rewrite local agent memory files and may remove context the user intended to keep. <br>
Mitigation: Run the default dry run first, review proposed changes, and use --backup before running with --apply. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/lokix94/peru-hub/tree/main/skills/memory-optimizer) <br>
- [ClawHub skill page](https://clawhub.ai/lokix94/skills/memory-optimizer-2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, code, guidance] <br>
**Output Format:** [Markdown reports, JSON analysis output, terminal summaries, and local markdown file edits when optimization is applied] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local workspace files; optimization defaults to dry run and modifies files only when --apply is used.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
