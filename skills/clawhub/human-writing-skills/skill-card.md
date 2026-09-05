## Description:

Advanced multilingual AI humanizer for natural rewriting, fiction editing, long-form audit and continuity, verified chunked agent review, translationese review, and character consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

Writers, editors, and developers use this skill to humanize AI-assisted drafts, compile genre-aware writing prompts, audit long-form continuity, verify rewrite fidelity, and produce staged review files for fiction, essays, news, academic, formal, legal, and technical prose.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool reads draft, ledger, source, original, and reference files explicitly supplied by the user.

Mitigation: Install and run it only for writing projects where those files are appropriate to expose to the local toolchain.

Risk: The optional MCP server can coordinate access to a writing project over local or HTTP transports.

Mitigation: Keep the MCP server rooted to the intended project and use loopback or bearer-authenticated HTTPS for HTTP mode.

Risk: Generated prompts and audit files can contain incomplete or incorrect editorial findings.

Mitigation: Review generated audit files before treating them as authoritative or applying changes to source drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [README](artifact/README.md)
- [Chunked Long-Form Audit, Style Unification, and Character Consistency](artifact/docs/long-form-consistency.md)
- [Multi-Stage Audit Pipeline](artifact/docs/audit-pipeline.md)
- [Agent Orchestration And MCP](artifact/docs/agent-orchestration.md)
- [Protected Content Verification](artifact/docs/protected-content.md)
- [Reference Style Alignment](artifact/docs/reference-style.md)
- [Fidelity, Statistics, and Conservative Fixes](artifact/docs/editing-tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions, compiled prompts, command examples, JSON diagnostics, and staged audit files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read user-selected draft, ledger, source, original, and reference files; optional MCP mode coordinates project-local task receipts.]

## Skill Version(s):

0.15.1 (source: server release evidence and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
