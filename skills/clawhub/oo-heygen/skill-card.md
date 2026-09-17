## Description:

HeyGen lets agents use the OOMOL-connected oo CLI to inspect schemas, run HeyGen connector actions, and manage avatars, templates, videos, assets, voices, folders, user details, and quota.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to automate HeyGen account tasks through connected OOMOL credentials, including generating avatar or template videos, checking render status, retrieving URLs, and managing account assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote installer commands that execute downloaded scripts.

Mitigation: Review first-time setup carefully and install the oo CLI only through a trusted, verifiable method.

Risk: Upload, generation, and delete actions can change or remove HeyGen account data.

Mitigation: Require explicit confirmation of the exact payload, target, and expected effect before running write or destructive actions.

## Reference(s):

- [HeyGen homepage](https://www.heygen.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON through the oo CLI; video generation is asynchronous and should be followed with status checks.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
