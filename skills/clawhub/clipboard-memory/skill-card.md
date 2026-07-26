## Description: <br>
Clipboard Memory helps an agent recall and recover clipboard history on macOS from the local clipmem archive, including text, commands, URLs, file paths, HTML, images, PDFs, and binary exports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users on macOS use this skill when they need to find, inspect, restore, or export something previously copied to the local clipboard. It is intended for narrow clipboard-history recall before using broader web, repository, or filesystem search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clipboard history can contain passwords, tokens, private messages, documents, images, and file paths. <br>
Mitigation: Use narrow queries and filters, surface only the minimum matching content needed, and avoid broad exports or summaries of unrelated clipboard entries. <br>
Risk: Commands such as export, restore, forget, purge, settings, service, launch-at-login, and update-check can disclose, overwrite, delete, or change local clipboard and app state. <br>
Mitigation: Treat these as explicit user-intent operations; inspect candidates or use dry-run/detail commands where available before making broad mutations. <br>
Risk: Empty or weak results may reflect a stale watcher, inaccessible database, or overly narrow filters rather than absence of copied content. <br>
Mitigation: Check setup health and pagination or broaden the query before concluding that no matching clipboard item exists. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/clipboard-memory) <br>
- [Publisher profile](https://clawhub.ai/user/tristanmanchester) <br>
- [Clipboard Memory Commands Reference](references/commands.md) <br>
- [Clipboard Memory JSON Schema](references/json-schema.md) <br>
- [Clipboard Memory Worked Examples](references/examples.md) <br>
- [Clipboard Memory Setup Check](references/setup-check.md) <br>
- [Clipboard Memory Troubleshooting](references/troubleshooting.md) <br>
- [Apple NSPasteboard documentation](https://developer.apple.com/documentation/appkit/nspasteboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON field references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local macOS clipmem results; retrieval commands should prefer --format json or toon and check pagination, confidence, and setup health before answering.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release metadata and openclaw metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
