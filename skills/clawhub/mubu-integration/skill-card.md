## Description: <br>
Mubu Integration helps agents authenticate with Mubu, manage documents and folders, and import or export outlines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuboacean](https://clawhub.ai/user/liuboacean) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agents use this skill to perform explicit Mubu note operations such as listing, creating, saving, moving, searching, and converting outline documents between Mubu structures and Markdown, OPML, or FreeMind XML. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Mubu account credentials and a local token to access real Mubu documents. <br>
Mitigation: Install only if account-level Mubu access is acceptable, keep MUBU_PHONE, MUBU_PASSWORD, and ~/.mubu_token private, and use the skill only for explicit Mubu actions. <br>
Risk: Save, move, delete, and purge operations can affect real remote content, and purge is irreversible. <br>
Mitigation: Review document and folder IDs before action, rely on the guarded soft-delete workflow for delete, and treat purge --yes as a deliberate irreversible operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration) <br>
- [README](README.md) <br>
- [Weekly outline example](examples/weekly.md) <br>
- [Mubu API base endpoint](https://api2.mubu.com/v3/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, CLI text, shell commands, OPML, and FreeMind XML] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-stream agent responses and CLI output; document exports may include Markdown, JSON, OPML, or FreeMind XML.] <br>

## Skill Version(s): <br>
1.3.6 (source: server release metadata and scripts/mubu/__init__.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
