## Description: <br>
Xhs Note Analyzer retrieves public Xiaohongshu note details and helps creators analyze engagement, cover visuals, account positioning, tags, and optimization opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[if530770](https://clawhub.ai/user/if530770) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, brand and MCN operators, and content planners use this skill to query one or more public Xiaohongshu note IDs or full links, inspect note metadata and engagement snapshots, and receive actionable content optimization analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles a RedFoxHub API key and note-account data. <br>
Mitigation: Treat REDFOX_API_KEY as a secret, prefer a scoped or revocable key when available, and do not expose it in code, prompts, logs, or output files. <br>
Risk: The skill may send note content, URLs, images, and engagement data to the provider for retrieval and analysis. <br>
Mitigation: Review the note data and media being submitted before use, especially for sensitive creator, brand, or campaign information. <br>
Risk: The security verdict flags under-scoped network and file actions around note retrieval and remote-image handling. <br>
Mitigation: Install only from a trusted publisher, review generated commands before execution, and confirm before allowing deletes, updates, bulk actions, or remote-image downloads. <br>


## Reference(s): <br>
- [Xhs Note Analyzer on ClawHub](https://clawhub.ai/if530770/skills/xhs-note-analyzer) <br>
- [Core Workflow](artifact/references/core_workflow.md) <br>
- [RedFoxHub API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis with structured note-detail fields and JSON returned by the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-note and comma-separated batch inputs; short xhslink.com URLs are not supported.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
