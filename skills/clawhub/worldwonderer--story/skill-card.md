## Description:

Routes Chinese web novel requests to the matching writing skill and can launch a local project dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Chinese-language web novel authors use it to route writing, story analysis, trend research, manuscript review, imports, project questions, and author-preference requests to companion skills, or to open a local project dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates this release suspicious because an unauthenticated network mode may read, change, or delete workspace files.

Mitigation: Keep the Dashboard on its default loopback address and do not enable --allow-network or expose the workspace over a network.

Risk: The security scan reports an update command that uses an unpinned installer.

Mitigation: Review the update source and target before running update commands, and use a pinned release where available.

Risk: The scan is incomplete: 7 of 9 components were fully inspected, and static analysis of two files was partial.

Mitigation: Review the remaining package contents and scan report before installation.

## Reference(s):

- [Project link listed in the skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Project releases](https://github.com/zenstory-ai/oh-story-claudecode/releases)
- [Project changelog](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Natural-language responses and Markdown, with shell commands for local dashboard startup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes according to user intent; dashboard commands target a local workspace.]

## Skill Version(s):

1.0.36 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
