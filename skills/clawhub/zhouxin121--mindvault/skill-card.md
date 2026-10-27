## Description:

MindVault helps agent users archive conversations as local JSONL, extract durable rules, and create project snapshots across supported local frameworks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and users of supported local agent frameworks can archive conversations, extract reusable long-term rules, and restore project context with snapshots. The skill also offers an optional DRAS-V reflection workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WorkBuddy reader deliberately conceals a directory name to evade interception.

Mitigation: Ask the publisher to remove this behavior before installing, and explicitly select the source project, session, and output directory.

Risk: Archives retain sensitive conversation content, and backup guarantees may exceed what the code preserves.

Mitigation: Protect archives, keep original logs, and avoid concurrent exports.

Risk: Extracted rules could introduce incorrect or misleading guidance when reused.

Mitigation: Review extracted rules before reusing them.

## Reference(s):

- [MindVault release on ClawHub](https://clawhub.ai/zhouxin121/skills/mindvault)
- [MindVault project repository (listed in package metadata)](https://github.com/zhouxin121/mindvault)

## Skill Output:

**Output Type(s):** [JSONL, Markdown, Guidance, Shell commands]

**Output Format:** [Local JSONL conversation archives and Markdown memory/project snapshots, with procedural guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-triggered; documentation describes local file output.]

## Skill Version(s):

1.3.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
