## Description:

YuanGe routes tasks to combinations of YottaMeta skills, inventories installed skills, and installs or updates them across agent skill directories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use YuanGe to choose combinations from the YottaMeta skill family, see which skills are installed, and manage installation or updates across agent directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health checks can execute scripts from untrusted skill directories.

Mitigation: Until the doctor authorization fix is available, avoid running doctor on untrusted directories and review target directories before changes.

Risk: A crafted skill import can write outside the selected folder.

Mitigation: Prefer a release that fixes import containment, pin the installer version, and review directories before making changes.

Risk: The security scan was partial; downloaded skill packages and every bundled code path were not audited.

Mitigation: Review downloaded skill packages and the bundled code paths before use; avoid adopting unreviewed external skills.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Installation flow guide](references/install-flow.md)
- [Provider protocol guide](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON, Shell commands]

**Output Format:** [Text or JSON summaries, routing recommendations, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Install and update commands can change the selected skill directory; routing and inventory outputs are informational.]

## Skill Version(s):

0.30.10 (source: frontmatter, CHANGELOG, package.json; released 2026-11-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
