## Description:

Searches Windows local files, folders, and Codex rollout JSONL logs through Everything SDK IPC or local HTTP JSON, returning full paths without opening the Everything GUI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssesweb](https://clawhub.ai/user/ssesweb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users on Windows use this skill to locate local files, folders, and Codex session logs through an existing Everything index, especially when they need complete paths or Everything search syntax.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can load a native Everything SDK DLL from --dll or EVERYTHING_SDK_DLL, which could execute untrusted native code if pointed at an unsafe file.

Mitigation: Use the bundled verified SDK payloads or only an architecture-matched DLL from a trusted source.

Risk: Everything searches can enumerate indexed local paths and Codex session log locations.

Mitigation: Run searches only for requested targets and avoid echoing secrets, cookies, tokens, or unrelated private log content.

Risk: Everything HTTP access may expose local index queries if bound beyond localhost.

Mitigation: Keep the Everything HTTP service bound to 127.0.0.1, localhost, or ::1 and do not expose unauthenticated access to a network.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssesweb/skills/everything-search-ipc)
- [Everything SDK source package](https://www.voidtools.com/Everything-SDK.zip)
- [Bundled Everything SDK source notes](artifact/assets/everything-sdk/SOURCE.txt)
- [Bundled Everything SDK license notes](artifact/assets/everything-sdk/LICENSE.txt)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text paths or JSON search results, with Markdown guidance for agent usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are bounded by limit and offset arguments; JSON output includes path and type fields.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
