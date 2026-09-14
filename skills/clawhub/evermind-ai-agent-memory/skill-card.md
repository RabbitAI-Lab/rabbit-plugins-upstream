## Description:

Evermind helps AI agents recover cross-session memory by reading core identity, rules, todos, and work logs while using a local change index to avoid rereading unchanged files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Evermind to help SKILL.md-compatible agents resume long-running work across sessions, preserve user rules and todos, and reduce repeated context-loading cost. It is intended for local workflows where persistent agent memory and handover files are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist workspace instructions as future agent rules and can optionally intercept tool actions.

Mitigation: Review AGENTS.md, CLAUDE.md, config.yaml, and generated .evermind/rules.json before enabling automatic recovery or hook-based enforcement in an untrusted repository.

Risk: A wildcard PreToolUse hook could apply rule checks to broad tool activity before rules are approved.

Mitigation: Avoid enabling the wildcard PreToolUse hook until the stored rules have been reviewed and are kept in a trusted location.

Risk: Persistent local memory files may retain sensitive project or user context.

Mitigation: Install only for workflows where local persistent memory is desired, and review the files written under .evermind as part of normal repository hygiene.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ccy123abcd/skills/evermind-ai-agent-memory)
- [Publisher Profile](https://clawhub.ai/user/ccy123abcd)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [Automatic Recovery Snippet](artifact/assets/agents-snippet.md)
- [Example Configuration](artifact/config.example.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and YAML/JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to create or update local memory index, rule, and handover files under .evermind when the workflow is followed.]

## Skill Version(s):

0.4.4 (source: frontmatter, changelog released 2026-09-14, version file, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
