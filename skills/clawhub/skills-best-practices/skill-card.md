## Description: <br>
Build high-quality Agent Skills for Claude following official Anthropic best practices. Covers SKILL.md structure, frontmatter, description writing, progressive disclosure, testing, patterns, troubleshooting, and distribution across all surfaces (Claude.ai, Claude Code, API, Agent SDK). Use when creating a skill, reviewing skill quality, debugging why a skill won't trigger, structuring skill directories, or writing skill descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create, review, troubleshoot, test, and publish Agent Skills for Claude and ClawHub. It provides practical guidance for SKILL.md structure, descriptions, progressive disclosure, reference organization, validation, security considerations, and distribution across supported surfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example shell, ClawHub CLI, API, MCP, or dynamic-injection commands may be copied into a user's own environment without review. <br>
Mitigation: Review and approve any example commands before running them, and scan skills before deployment. <br>
Risk: Documentation about dynamic-injection syntax can be hazardous if copied into a load-time context where it may execute. <br>
Mitigation: Keep dynamic-injection examples in reference files or otherwise separate trigger syntax from executable load-time content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/skills-best-practices) <br>
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/skills-best-practices) <br>
- [Description writing guide](references/description-guide.md) <br>
- [Patterns and workflows](references/patterns.md) <br>
- [Claude Code features](references/claude-code-features.md) <br>
- [Quality checklist](references/checklist.md) <br>
- [ClawHub publishing](references/clawhub-publishing.md) <br>
- [Agent Skills Spec](https://agentskills.io/specification) <br>
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills) <br>
- [API Skills Guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide) <br>
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) <br>
- [Anthropic Skills Repo](https://github.com/anthropics/skills) <br>
- [Engineering Blog: Agent Skills](https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills) <br>
- [Complete Guide PDF](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with examples, checklists, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no bundled executables or hidden automatic behavior were found in security evidence.] <br>

## Skill Version(s): <br>
0.6.3 (source: server release evidence, SKILL.md metadata, and changelog, released 2026-07-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
