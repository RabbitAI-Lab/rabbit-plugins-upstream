## Description:

An AI litigation desk assistant for lawyers and in-house counsel that supports statute lookup, similar-case research, damages and fee calculations, legal document drafting, and document review with source-linked outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal practitioners and in-house counsel use this skill to research statutes and cases, analyze litigation materials, calculate litigation fees or damages, draft and review legal documents, and produce source-linked legal research reports. Outputs are intended as attorney-reviewed working drafts and research aids, not final legal opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to handle a Cue API key and modify local AI-client configuration.

Mitigation: Review configuration changes before use, avoid sharing long-lived secrets in chat, and rotate or revoke credentials if exposed.

Risk: The skill can upload selected legal files to Cue services, which may include confidential or regulated matter data.

Mitigation: Confirm client and firm policy before upload, minimize or redact sensitive material where feasible, and use explicit upload consent.

Risk: The skill may run code pulled from external repositories and save reports locally.

Mitigation: Prefer a pinned or packaged runner, review scripts before execution, and store generated reports in an approved location.

Risk: Legal outputs may be incomplete or incorrect if used without professional review.

Mitigation: Treat outputs as drafts or research aids and require attorney review before filing, signing, or advising clients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-litigation-lawyer-assistant)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue statute MCP endpoint](https://mcp.cuecue.cn/api/statute/mcp/)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner repository mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown legal research reports, legal-document drafts, shell commands, and JSON configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated Markdown reports locally and may optionally produce DOCX files after user confirmation.]

## Skill Version(s):

1.7.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
