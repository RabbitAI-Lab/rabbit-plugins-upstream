## Description:

Shisan Xinuo Workflow guides coding agents through auditable engineering workflows with task routing, quality gates, rollback discipline, memory templates, and platform adaptation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxc663](https://clawhub.ai/user/zxc663)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to make agent work on coding, review, bug-fix, multi-file, and cross-module tasks more disciplined and auditable. It is intended for hands-on engineering work, not general chat, single-file read-only lookup, or unrelated Q&A.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently alter agent rule and memory files across projects and sessions.

Mitigation: Install only when that behavior is desired; prefer project-scoped or on-demand injection and review diffs, backups, and uninstall steps before use.

Risk: Global hard injection and hooks can broaden the workflow's effect beyond the intended project.

Mitigation: Avoid global hard injection and hooks unless the exact files and hook behavior have been reviewed and constrained to the intended workspace.

Risk: Automatic memory or rule-file creation may be unacceptable in some repositories.

Mitigation: Do not use the skill in repositories where automatic creation or modification of rule or memory files is not allowed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxc663/skills/shisan-xinuo-workflow)
- [Source homepage](https://github.com/zxc663/shisan-xinuo-workflow)
- [Workflow and quality gates](references/workflows.md)
- [Platform adaptation](references/platform-adaptation.md)
- [Security and rollback guidance](references/security.md)
- [OWASP GenAI LLM Top 10](https://genai.owasp.org/)
- [SLSA](https://slsa.dev/)
- [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions and templates with occasional shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project rule, memory, planning, review, rollback, and hook template files when applied by an agent.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact metadata reports 2.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
