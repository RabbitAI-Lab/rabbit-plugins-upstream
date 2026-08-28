## Description:

Provides sanitization guidelines for external content in skills and hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to handle untrusted external content from web, GitHub, URL, and user-provided sources with clear sanitization and code-execution prevention guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume this package performs automated sanitization by itself.

Mitigation: Treat this release as documentation-only guidance and review any separate plugin or hook that performs automated sanitization before use.

Risk: Untrusted external content can carry prompt-injection or unsafe code-execution patterns.

Mitigation: Apply the documented size limits, tag and instruction stripping, boundary markers, hidden-text removal, and code-execution prevention checks before using external content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-content-sanitization)
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no executable behavior is included in this package.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
