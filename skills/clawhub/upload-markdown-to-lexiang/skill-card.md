## Description: <br>
Upload a Markdown document with local images and formulas to an editable Tencent Lexiang page, with local preflight, deterministic mixed text/image upload, and remote verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajaxhe](https://clawhub.ai/user/ajaxhe) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to publish Markdown documents, local images, formulas, and supported callout markup to Tencent Lexiang pages through a shared CLI. It is intended for workflows that need repeatable preflight checks, page creation or overwrite, and post-upload verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a Lexiang personal MCP token locally and uses it to create or overwrite user-selected Lexiang pages. <br>
Mitigation: Use dry-run first for new workflows, keep credential files private, and prefer a named profile or dedicated credential with the least Lexiang access needed. <br>
Risk: An incorrect parent_id or entry_id can publish to the wrong location or overwrite an existing Lexiang page. <br>
Mitigation: Review the target parent_id or entry_id before upload and rely on the built-in local preflight and remote verification before treating the upload as complete. <br>


## Reference(s): <br>
- [CLI Contract](references/cli-contract.md) <br>
- [Lexiang personal credential page](https://lexiangla.com/ai/claw) <br>
- [ClawHub skill page](https://clawhub.ai/ajaxhe/skills/upload-markdown-to-lexiang) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and CLI JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI emits a page URL or stable JSON including action, entry_id, page_url, verification counts, credential profile, cli_api, and version; diagnostics and progress are written to stderr.] <br>

## Skill Version(s): <br>
1.3.1 (source: SKILL.md frontmatter, README.md, CLI contract, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
