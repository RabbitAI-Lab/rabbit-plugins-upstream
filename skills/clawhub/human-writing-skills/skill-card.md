## Description:

Advanced Human Writing & AI Humanizer helps agents humanize AI-shaped drafts, perform natural rewriting, edit fiction and long-form documents, and audit continuity, voice, translationese, protected content, citations, and source fidelity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and writing teams use this skill to compile focused writing prompts, humanize or revise drafts, audit long-form manuscripts and reports, coordinate bounded agent reviews, and verify source-sensitive rewrites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote MCP access could expose manuscript or business documents if it is bound to a public network without proper controls.

Mitigation: Keep MCP on stdio or 127.0.0.1 when possible; if remote access is required, use HTTPS, bearer authentication, and a project root that excludes unrelated sensitive files.

Risk: Writing audits and generated prompts can miss omissions or produce incorrect editorial guidance.

Mitigation: Review findings in context, run verification workflows for source-sensitive rewrites, and use coverage receipts before final long-form reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [README](README.md)
- [Agent Orchestration And MCP](docs/agent-orchestration.md)
- [Chunked Long-Form Audit, Style Unification, and Character Consistency](docs/long-form-consistency.md)
- [Protected Content Verification](docs/protected-content.md)
- [Deterministic Writing-Pattern Linter](docs/pattern-linter.md)
- [Fidelity, Statistics, and Conservative Fixes](docs/editing-tools.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, CLI command examples, generated prompt text, audit files, JSON reports, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can emit staged audit packages, deterministic lint findings, statistics, conservative fix previews, protected-content verification results, and local MCP coordination outputs.]

## Skill Version(s):

0.15.2 (source: pyproject.toml and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
