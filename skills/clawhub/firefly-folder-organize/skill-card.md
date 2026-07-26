## Description: <br>
Firefly Folder Organize lets an agent connect to the local Firefly AI Folder desktop app to query file analysis metadata, search files, monitor analysis progress, and prepare virtual directory organization plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leonard-li777](https://clawhub.ai/user/leonard-li777) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an AI agent interact with Firefly AI Folder's local API for workspace summaries, file metadata lookup, semantic search, progress monitoring, and organization-plan drafting. The user should review generated organization plans in the desktop app before applying them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose workspace paths, filenames, file metadata, search results, and organization prompt data through the local Firefly AI Folder API. <br>
Mitigation: Install and invoke it only for explicit Firefly-specific requests, and avoid using it with sensitive workspaces unless that information is acceptable in the active AI conversation. <br>
Risk: The security summary flags broad triggers and forceful prompt/output instructions that deserve review before installation. <br>
Mitigation: Review the skill instructions and scanner summary before deployment, and prefer narrow user requests that clearly target Firefly AI Folder operations. <br>
Risk: Organization plans may be incomplete, incorrect, or misaligned with user intent before they are sent to the desktop app. <br>
Mitigation: Preview and review proposed organization plans in the desktop app before applying them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leonard-li777/skills/firefly-folder-organize) <br>
- [Server-resolved source repository](https://github.com/Leonard-Li777/ai-folder-organize) <br>
- [Claw metadata homepage](https://github.com/Leonard-Li777/ai-folder-organize) <br>
- [Firefly AI Folder desktop repository](https://github.com/Leonard-Li777/firefly-ai-folder-desktop) <br>
- [Skill API reference](REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with JSON snippets and JavaScript or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local API responses, workspace paths, filenames, file metadata, search results, progress summaries, and organization-plan guidance surfaced in the active AI conversation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
