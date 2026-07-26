## Description: <br>
Chezmoi helps agents manage chezmoi dotfiles through interactive diff review, template consolidation, cross-platform diagnostics, environment checks, and MCP server synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review and apply chezmoi dotfile changes safely, consolidate duplicated templates, troubleshoot macOS and Windows compatibility, validate required helper files, and keep MCP server configuration synchronized across tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled launcher can start Claude with permission checks disabled and resumed context. <br>
Mitigation: Review before installing and remove or edit bin/claude-source.sh unless that persistent launcher behavior is intentionally required. <br>
Risk: Dotfile and MCP configuration changes can propagate across multiple local tools. <br>
Mitigation: Run and review chezmoi diff before applying changes, and get explicit user approval for the affected files. <br>
Risk: Secrets or tokens could be stored in chezmoi-managed files during MCP or UTCP configuration work. <br>
Mitigation: Do not store plaintext tokens in managed files; prefer environment variables or a dedicated secret-management flow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/chezmoi) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Apply Guide](artifact/apply.md) <br>
- [Diff Required Guide](artifact/diff-required.md) <br>
- [Cross-Platform Guide](artifact/cross-platform.md) <br>
- [MCP Sync Guide](artifact/mcp-sync.md) <br>
- [Doctor Guide](artifact/doctor.md) <br>
- [Template Consolidation Guide](artifact/consolidate.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, TOML snippets, and review prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user approval before applying chezmoi changes; outputs may include file-specific apply choices and configuration edits.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata and changelog, released 2026-07-07) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
