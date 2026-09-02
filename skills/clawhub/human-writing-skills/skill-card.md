## Description:

Advanced multilingual AI humanizer for natural rewriting, fiction editing, long-form audit and continuity, verified chunked agent review, translationese review, and character consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whh110112](https://clawhub.ai/user/whh110112)

### License/Terms of Use:

MIT

## Use Case:

External users, writers, editors, and developers use this skill to humanize AI-shaped drafts, rewrite while preserving meaning, edit fiction and serious prose, and audit long-form continuity, voice, sources, numbers, and translation fidelity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local writing and editing tools can read drafts and reference files and write generated audit packages.

Mitigation: Install only for intended writing projects, keep MCP roots scoped to those projects, and review generated files before relying on them.

Risk: Generated prompts and audit packages may contain sensitive draft text, source excerpts, or protected content supplied by the user.

Mitigation: Review prompts before sending them to model or API sessions and use the protected-content verification workflow when preserving source meaning matters.

Risk: The optional HTTP MCP endpoint can expose project coordination capabilities if made public.

Mitigation: Do not expose the endpoint publicly without HTTPS and a strong bearer token.

Risk: The editorial modules provide writing guidance and audits, not proof of authorship or guaranteed detector outcomes.

Mitigation: Frame results as editing evidence and quality guidance rather than authorship attribution or detector evasion.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/whh110112/skills/human-writing-skills)
- [README](README.md)
- [Agent Orchestration And MCP](docs/agent-orchestration.md)
- [Multi-Stage Audit Pipeline](docs/audit-pipeline.md)
- [Chunked Long-Form Audit, Style Unification, and Character Consistency](docs/long-form-consistency.md)
- [Fidelity, Statistics, and Conservative Fixes](docs/editing-tools.md)
- [Protected Content Verification](docs/protected-content.md)
- [Reference Style Alignment](docs/reference-style.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prompts, audit reports, CLI output, and generated project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write staged audit packages, coverage receipts, conservative fix previews, and local MCP coordination artifacts.]

## Skill Version(s):

0.14.1 (source: release metadata and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
