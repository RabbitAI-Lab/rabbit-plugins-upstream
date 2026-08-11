## Description:

Skills Best Practices guides agents in creating, reviewing, debugging, structuring, and publishing high-quality Agent Skills across Claude.ai, Claude Code, API, Agent SDK, and ClawHub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and reviewers use this skill to write, assess, troubleshoot, and publish portable Agent Skills with clear frontmatter, concise instructions, validation checks, and ClawHub publishing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples may include commands that contact ClawHub or use a ClawHub token.

Mitigation: Review commands and token usage before execution; run only commands appropriate for the active publisher account and environment.

Risk: Skill-authoring guidance can become stale as Agent Skills, Claude Code, API, and ClawHub behavior changes.

Mitigation: Validate against current official documentation and run the recommended skill validator before publishing or relying on version-specific guidance.

Risk: Incorrect or overly broad guidance could cause a generated skill to trigger at the wrong time or include unsafe examples.

Mitigation: Test triggering, review examples, and scan the final skill before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/skills-best-practices)
- [Source Homepage](https://github.com/tenequm/skills/tree/main/skills/skills-best-practices)
- [ClawHub Publishing Reference](references/clawhub-publishing.md)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [Anthropic Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline examples, YAML snippets, command examples, checklists, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; it does not install code or run commands automatically.]

## Skill Version(s):

0.8.0 (source: evidence.release.version, SKILL.md metadata.version, CHANGELOG released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
