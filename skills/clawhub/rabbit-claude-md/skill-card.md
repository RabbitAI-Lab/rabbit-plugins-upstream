## Description:

Audit, tighten, and restructure CLAUDE.md and AGENTS.md memory files so the root file stays a short "where am I" plus rules instead of a changelog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to audit and improve AI agent memory files such as CLAUDE.md and AGENTS.md. It helps keep root memory files concise, separates deeper context into appropriate locations, and produces evidence-backed findings with disposition plans before edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hook and rewrite capabilities can affect commit or PR text.

Mitigation: Enable Claude hook integration only when you explicitly want it to inspect prose writes and command text.

Risk: Model-assisted rewriting can send document passages and configured credentials to a user-selected endpoint.

Mitigation: Use --apply-model only after confirming the endpoint and reviewing the configured RABBIT_MODEL_API_KEY handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whit3rabbit/skills/rabbit-claude-md)
- [Criteria](references/criteria.md)
- [Templates](references/templates.md)
- [Restructure](references/restructure.md)
- [Craft](references/craft.md)
- [ASD-STE100 Simplified Technical English](references/ste.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown findings, disposition tables, proposed diffs, shell commands, and targeted file edits when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read repository memory files and, when explicitly invoked with model-assisted rewrite options, may use a user-configured OpenAI-compatible endpoint.]

## Skill Version(s):

0.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
