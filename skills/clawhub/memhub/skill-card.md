## Description:

MemHub manages a user-specified cross-agent memory repository with MemHub Protocol v0.1, supporting memory reads, writes, search, context export, and GitHub or Gitee synchronization when requested by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use MemHub to preserve, retrieve, archive, export, and synchronize long-term personal memory across agents. The skill is intended for explicit user-directed memory operations and for configured GitHub or Gitee synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist personal memory locally and optionally synchronize it through GitHub or Gitee credentials.

Mitigation: Use a dedicated MEMHUB_REPO, review memory content before enabling automatic memory policies, keep the remote repository private, and choose --manual-sync when automatic network sync is not wanted.

Risk: OAuth tokens, personal access tokens, client secrets, and broker-based authorization can expose sensitive account access if mishandled.

Mitigation: Treat .memhub/secrets.yaml and all OAuth or PAT credentials as sensitive, avoid sharing credentials in chat or committed files, and use only trusted Gitee OAuth brokers.

## Reference(s):

- [MemHub ClawHub release page](https://clawhub.ai/cutd/skills/memhub)
- [MemHub README](artifact/README.md)
- [MemHub skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and command-line text with generated memory files and context exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local YAML and Markdown memory files, Git commits, exported context packs, and synchronization configuration when explicitly requested.]

## Skill Version(s):

0.4.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
