## Description:

Searches and navigates stored knowledge in memory palaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to find concepts, cross-reference stored information, and navigate search results across memory-palace knowledge stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation triggers may cause the skill to surface during ordinary search or recall requests.

Mitigation: Use narrower activation terms or disable the skill when working outside the memory-palace workflow.

Risk: Search guidance can return stale, incomplete, or misleading memory-palace entries if the underlying palace indices are outdated.

Mitigation: Rebuild or update indices after meaningful palace changes and review retrieved entries before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-memory-palace-knowledge-locator)
- [Memory Palace Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace)
- [Index Structure](modules/index-structure.md)
- [Search Strategies](modules/search-strategies.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; no hidden execution, credential access, exfiltration, or destructive behavior found in security evidence.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
