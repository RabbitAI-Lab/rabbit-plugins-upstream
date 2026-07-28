## Description: <br>
Edit Calibre title, authors, series, tags, dates, comments, and analysis metadata with dry-run/apply gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextaltair](https://clawhub.ai/user/nextaltair) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and library maintainers use this skill to update Calibre book metadata such as titles, authors, series, tags, dates, comments, and analysis fields with confirmation, dry-run, and apply steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify Calibre metadata and requires access to a Calibre library. <br>
Mitigation: Keep credentials in environment variables, review dry-runs before apply, and apply changes only after explicit user approval. <br>
Risk: The skill may read document content, use web evidence, or delegate extracted evidence for heavy proposal generation. <br>
Mitigation: Keep analysis local unless the user explicitly approves sharing book excerpts or evidence with a subagent. <br>
Risk: Low-confidence or conflicting metadata proposals could overwrite useful existing fields if applied without review. <br>
Mitigation: Use the documented pending-review flow for unresolved items and apply only approved, high-confidence fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/calibre-metadata-apply) <br>
- [Publisher profile](https://clawhub.ai/user/nextaltair) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSONL change plans and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, calibredb, CALIBRE_PASSWORD, and explicit user approval before applying metadata writes.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
