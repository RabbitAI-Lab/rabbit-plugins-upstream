## Description:

HeyGen enables agents to read, create, update, and delete HeyGen data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HeyGen through an OOMOL-connected account, including reading account resources, starting video generation jobs, uploading assets, and deleting assets or videos when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt installation of the oo CLI through one-line curl or PowerShell commands.

Mitigation: Review the official oo CLI installation instructions before running installer commands.

Risk: Write actions can upload assets or start HeyGen video generation jobs that affect account quota or content state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: Destructive actions can delete HeyGen assets or generated videos.

Mitigation: Require explicit approval for the exact target before running destructive actions.

Risk: HeyGen account access is mediated through OOMOL-connected credentials.

Mitigation: Install only when the user is comfortable using OOMOL as the intermediary for the connected HeyGen account.

## Reference(s):

- [HeyGen homepage](https://www.heygen.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-heygen)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns command guidance and oo connector results, including JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
