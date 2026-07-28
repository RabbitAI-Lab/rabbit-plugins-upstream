## Description: <br>
Calibre catalog search, ID lookup, book viewing, and one-book analysis. Read-only; metadata edits use calibre-metadata-apply. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent search a Calibre library, inspect book records by ID, view book details, and run a one-book analysis workflow when the user explicitly asks for reading or analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is described as read-only, but the one-book analysis workflow can write analysis into Calibre comments metadata. <br>
Mitigation: Use list, search, and ID viewing for lookup-only requests; run the analysis/comments workflow only after explicit user intent and verify the target book and run state before applying results. <br>
Risk: The workflow can retain extracted full book text and analysis data in local state/cache files and a SQLite database. <br>
Mitigation: Run it from a controlled workspace, treat cache and database contents as sensitive book content, and clear bundled or generated state/cache files before publishing or sharing. <br>
Risk: Scripts may load Calibre connection settings and credentials from the current directory .env or ~/.openclaw/.env. <br>
Mitigation: Run from the intended directory and provide CALIBRE_PASSWORD through a controlled environment so unrelated .env files are not loaded accidentally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/calibre-catalog-read) <br>
- [README](README.md) <br>
- [Subagent analysis prompt](references/subagent-analysis.prompt.md) <br>
- [Subagent analysis output schema](references/subagent-analysis.schema.json) <br>
- [Subagent input schema](references/subagent-input.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command results; one-book analysis output is schema-bound JSON that can be rendered into Calibre comments.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, uv, calibredb, ebook-convert, and CALIBRE_PASSWORD; may use CALIBRE_USERNAME and Calibre connection environment variables.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
