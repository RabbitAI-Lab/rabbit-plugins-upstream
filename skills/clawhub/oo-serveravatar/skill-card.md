## Description:

ServerAvatar helps agents read ServerAvatar organizations, servers, applications, and databases through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect ServerAvatar organizations and inventory servers, applications, and databases through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that fetch and execute scripts.

Mitigation: Review official installation documentation, prefer a pinned or package-manager install, and do not let an agent automatically run curl-to-bash or Invoke-Expression commands.

Risk: Using the skill depends on OOMOL handling ServerAvatar access for the connected account.

Mitigation: Install only if that credential handling model is acceptable, and review the connected ServerAvatar scopes before use.

## Reference(s):

- [ServerAvatar homepage](https://serveravatar.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; read actions return data with meta.executionId.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
