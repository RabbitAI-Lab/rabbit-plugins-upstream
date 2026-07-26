## Description: <br>
Siluzan CSO helps agents use the Siluzan content operations platform for content drafting and revision, persona/styleGuide work, RAG-backed knowledge retrieval, social publishing, account operations, planning, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sigedev01-bit](https://clawhub.ai/user/sigedev01-bit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations teams and external agents use this skill to create and revise marketing content, manage account personas, retrieve CSO knowledge-base material, upload media, publish to supported social platforms, inspect publishing tasks, and review operating reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer may make broad lasting system changes and run remote code with limited user control. <br>
Mitigation: Review the installer before running it, prefer manual installation when appropriate, keep npm registry changes explicit, and avoid piping remote scripts directly into shells. <br>
Risk: CSO credentials, OAuth links, account snapshots, uploaded media, and publish actions are sensitive. <br>
Mitigation: Use intended credential storage, avoid exposing tokens in shell history or shared files, and confirm target accounts and content before upload, account changes, retries, deletes, or publishing. <br>
Risk: Publishing, planning, and account-management commands can change external platform state. <br>
Mitigation: Require user confirmation for write actions and verify account IDs, media assets, platform selection, and scheduled content before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sigedev01-bit/skills/siluzan-cso) <br>
- [Siluzan homepage](https://www.siluzan.com) <br>
- [Setup and authentication](references/setup.md) <br>
- [Publishing workflow](references/publish.md) <br>
- [RAG knowledge retrieval](references/rag.md) <br>
- [Content writing workflow](three-lib-content-workflow/content-writer.workflow.md) <br>
- [Persona management](references/persona.md) <br>
- [Task management](references/task.md) <br>
- [Reporting](references/report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, JSON configuration examples, and local file outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local validation files, media cover images, account snapshots, and publishing configuration artifacts when the user confirms the relevant operation.] <br>

## Skill Version(s): <br>
1.1.33 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
