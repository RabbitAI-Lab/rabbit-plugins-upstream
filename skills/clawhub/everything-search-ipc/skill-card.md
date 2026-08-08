## Description: <br>
Everything 本地搜索 helps agents search Windows files, folders, and Codex session JSONL logs through the Everything SDK IPC interface and return full local paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssesweb](https://clawhub.ai/user/ssesweb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need an agent to locate local Windows files, folders, or Codex conversation logs through Everything search and return exact paths or JSON results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can search broad local file paths and sensitive Codex conversation logs. <br>
Mitigation: Install and run it only when local Everything index or Codex log search is intended, and avoid exposing prompts, secrets, file paths, or prior work history from returned results. <br>
Risk: The helper loads native Everything SDK DLLs, and custom DLL overrides can change what code is executed. <br>
Mitigation: Use the bundled verified DLL payloads or only architecture-matched DLL overrides from fully trusted sources. <br>
Risk: Search results depend on the Windows Everything service and its indexed state. <br>
Mitigation: Confirm Everything is running for the intended user context and review returned paths before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ssesweb/skills/everything-search-ipc) <br>
- [Publisher Profile](https://clawhub.ai/user/ssesweb) <br>
- [Everything SDK Source](https://www.voidtools.com/Everything-SDK.zip) <br>
- [Bundled Everything SDK Source Notice](artifact/assets/everything-sdk/SOURCE.txt) <br>
- [Bundled Everything SDK License Notice](artifact/assets/everything-sdk/LICENSE.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text paths, JSON search results, or Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include sensitive local file paths or Codex log locations; callers should limit queries and review outputs before sharing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
