## Description:

Dev Expert is a developer-assistant skill suite that routes software engineering requests to templates for project planning, API design, debugging, code generation and review, refactoring, testing, documentation, front-end design, CMS development, and MySQL work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, review, debug, test, document, and operate software or website projects through task-specific guidance templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can preserve or externally publish sensitive project details without sufficiently clear opt-in, destination, or redaction rules.

Mitigation: Confirm any external destination before use, review content before export, and remove secrets, credentials, customer data, internal URLs, and deployment or account handoff details.

Risk: The skill may read project context and modify or create files as part of broad coding-assistant workflows.

Mitigation: Use it only in trusted workspaces, review proposed file changes, and run appropriate tests or scans before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/dev-expert)
- [Server-resolved source repository](https://github.com/ebandao777-oss/dev-expert)
- [Skill definition](artifact/SKILL.md)
- [Release README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, code snippets, shell commands, configuration examples, and structured guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify development files when the user asks for implementation work.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
