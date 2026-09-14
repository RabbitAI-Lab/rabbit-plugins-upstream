## Description:

A fully adaptive 12-dimension character agent that scans input in real time, stacks identities from an identity matrix library, and supports @-invocation and memory threads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run multi-domain, role-stacked conversations that adapt expert perspectives, cultural modules, and output formats to the current task. It is suited for cross-disciplinary analysis, structured creative transformation, fact-checking perspectives, and explicit @-invoked persona workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests Bash, Write, and Edit permissions even though the documented persona-stacking workflow does not require shell execution or file mutation.

Mitigation: Use or publish a permission-limited version that can read bundled references and optionally perform web fact-checking, and avoid sensitive workspaces unless mutation and shell permissions are removed or tightly controlled.

Risk: Role-stacked outputs may sound like professional authority even when the skill is only simulating a perspective.

Mitigation: Require responses to frame roles as viewpoints, avoid claims of credentials or institutional affiliation, and add explicit boundaries for medical, legal, financial, or other regulated advice.

Risk: Memory-thread behavior may create an impression of persistent recall beyond the current available context.

Mitigation: Treat memory threads as session context only, disclose when prior context is unavailable, and avoid using the skill with sensitive personal or organizational information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/adaptive-identity-agent)
- [ClawHub publisher profile](https://clawhub.ai/user/wangjiaocheng)
- [Character data](artifact/references/character-data.md)
- [Character requirements](artifact/references/character-requirements.md)
- [Dialogue examples](artifact/references/dialogue.md)
- [Identity matrix](artifact/references/identity-matrix.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown or structured text with identity-stack headers and task-specific sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are expected to expose the active identity stack, keep active identities to three or fewer, and mark uncertainty or capability limits when needed.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
