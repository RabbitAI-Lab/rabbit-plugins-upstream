## Description:

Amara helps agents operate an Amara account through the OOMOL oo CLI for video, subtitle, team, user, language, and activity workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent read and manage Amara videos, subtitles, source URLs, teams, users, languages, and activity through a connected OOMOL account. It supports read workflows plus confirmed write and destructive actions such as creating subtitles, updating video metadata, publishing or approving subtitles, and deleting video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts that may execute unverified code.

Mitigation: Prefer an official signed or otherwise verifiable oo CLI installation method before using the skill.

Risk: The skill can perform write and destructive Amara actions through a connected account.

Mitigation: Confirm the exact action, target, and JSON payload before any write, delete, publish, approve, or reject operation.

Risk: Installing the skill allows an agent to operate the user's Amara account through OOMOL.

Mitigation: Install only when the publisher is trusted and the user intends the agent to access the connected Amara account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-amara)
- [Amara Homepage](https://amara.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amara Icon](https://static.oomol.com/logo/third-party/Amara.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to validate action payloads before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
