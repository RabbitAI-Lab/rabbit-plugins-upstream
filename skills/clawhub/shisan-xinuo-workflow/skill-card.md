## Description:

A workflow-governance agent skill that guides engineering tasks through tiered execution paths, required restatements, evidence checks, quality gates, rollback discipline, project memory practices, and prompt-injection/security review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to run coding, debugging, review, and multi-file project work through auditable workflow discipline. It is most useful when a task benefits from explicit scope restatement, workflow level selection, implementation records, verification gates, rollback planning, and security-aware delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist workflow behavior by creating or changing project memory, documentation, and agent rule files.

Mitigation: Prefer on-demand use unless persistent every-session behavior is intentional, and review target paths and diffs before accepting rule or memory changes.

Risk: Persistent workflow injection can affect future sessions or shared-project collaborators if installed globally or broadly.

Mitigation: Keep installation scoped to the intended project, decline hard injection when unnecessary, and review shared-project rule changes before committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Project homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow overview](SKILL.md)
- [Global agent workflow core](references/injection-core.md)
- [Workflow rules](references/rules.md)
- [Security and rollback](references/security.md)
- [Task workflows and quality gates](references/workflows.md)
- [Platform adaptation](references/platform-adaptation.md)
- [Skill usage guidance](references/skill-usage.md)
- [OWASP GenAI LLM Top 10](https://genai.owasp.org/)
- [SLSA](https://slsa.dev/)
- [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance, file templates, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify project memory, documentation, hook examples, and agent rule files when the workflow is applied.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; skill metadata.version: 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
