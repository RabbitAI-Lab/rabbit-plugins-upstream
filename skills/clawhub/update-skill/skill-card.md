## Description:

Update Skill helps developers refresh one skill in a skills repository by researching usage, upstream changes, and documentation, proposing gated edits, updating versioning and changelogs, validating changes, and preparing commit and publish steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and skill maintainers use this skill to perform an agent-assisted refresh of a specific repository skill, including research, gated edits, changelog and version updates, validation, privacy scanning, and commit or publish review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can modify repository skills and prepare commits or pushes.

Mitigation: Review the Phase 3 proposal before approving edits and review the Phase 6 diff before approving commit or push steps.

Risk: Research or usage findings could introduce private details into a public skill update.

Mitigation: Use the required privacy scan and drop private-scope findings before commit review.

Risk: Agent-proposed changes could introduce incorrect or misleading skill guidance.

Mitigation: Ground findings against primary sources, run the repository validation gate, and review generated changes before deployment.

## Reference(s):

- [Update Skill homepage](https://github.com/tenequm/skills/tree/main/skills/update-skill)
- [Pond MCP](https://pond.cascade.fyi/)
- [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown reports with command snippets, proposed file edits, validation results, diffs, and git or CI status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before edits and before commit or push steps.]

## Skill Version(s):

0.8.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
