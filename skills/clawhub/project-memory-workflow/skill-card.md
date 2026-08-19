## Description:

Maintain AI-readable project memory for software repositories across onboarding, initialization, context tracking, decisions, risks, and progress records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitzo](https://clawhub.ai/user/bitzo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to initialize and maintain repository memory files so agents can preserve project context, conventions, decisions, verification history, and risks across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic init triggers and implicit invocation can activate the workflow during ambiguous initialization requests.

Mitigation: Confirm the user's intent before keeping generated documentation changes, and review proposed file changes before committing or relying on them.

Risk: Generated or updated project memory can become misleading if it records assumptions as facts.

Mitigation: Use repository evidence and command output, mark unknown or unverified behavior explicitly, and keep progress entries factual and compact.

Risk: Repository memory files could accidentally capture credentials, private URLs, tokens, or local secret values.

Mitigation: Review generated documentation for sensitive information and preserve the skill's rule to never write credentials, tokens, private URLs, or local secret values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bitzo/skills/project-memory-workflow)
- [Server-resolved source provenance](https://github.com/Bitzo/project-memory-skill/tree/main/skills/project-memory-workflow)
- [Agent instruction file compatibility](artifact/references/agent-file-compatibility.md)
- [Project memory file design](artifact/references/memory-file-design.md)
- [Progress entry template](artifact/references/progress-entry-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown documents, repository instruction files, and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update docs/PROJECT.md, docs/DEVELOPMENT.md, docs/PROGRESS.md, docs/DECISIONS.md, docs/README.md, AGENTS.md, and optional CLAUDE.md files.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
