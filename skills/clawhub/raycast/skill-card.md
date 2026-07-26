## Description: <br>
Build and maintain Raycast extensions using the Raycast API. Triggers on @raycast/api, List, Grid, Detail, Form, AI.ask, LocalStorage, Cache, showToast, and BrowserExtension. Use this repo's references/api/*.md files as the primary source of truth for component specs and API usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xaif](https://clawhub.ai/user/xaif) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to build and maintain Raycast extensions with React, TypeScript, and @raycast/api components. It provides implementation patterns and API references for Raycast UI, storage, feedback, AI, browser, OAuth, clipboard, and system utility features. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Raycast extensions may access sensitive browser, clipboard, preference, OAuth, file, or telemetry data when those APIs are used. <br>
Mitigation: Review generated code for those APIs, require explicit user intent, minimize collected data, and redact secrets before logging or telemetry. <br>
Risk: Generated extension actions may write or delete files or perform externally visible actions. <br>
Mitigation: Use Raycast confirmations for destructive or externally visible actions and review the behavior before deployment. <br>


## Reference(s): <br>
- [Raycast Extensions Skill](artifact/SKILL.md) <br>
- [Raycast Extension Examples](artifact/examples.md) <br>
- [List API Reference](artifact/references/api/list.md) <br>
- [Grid API Reference](artifact/references/api/grid.md) <br>
- [Detail API Reference](artifact/references/api/detail.md) <br>
- [Form API Reference](artifact/references/api/form.md) <br>
- [Actions API Reference](artifact/references/api/actions.md) <br>
- [AI API Reference](artifact/references/api/ai.md) <br>
- [Browser Extension API Reference](artifact/references/api/browser-extension.md) <br>
- [Clipboard API Reference](artifact/references/api/clipboard.md) <br>
- [OAuth API Reference](artifact/references/api/oauth.md) <br>
- [Preferences API Reference](artifact/references/api/preferences.md) <br>
- [Storage API Reference](artifact/references/api/storage.md) <br>
- [Caching API Reference](artifact/references/api/caching.md) <br>
- [System Utilities API Reference](artifact/references/api/system-utilities.md) <br>
- [Window Management API Reference](artifact/references/api/window-management.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with TypeScript and TSX code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links back to the specific artifact reference files used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
