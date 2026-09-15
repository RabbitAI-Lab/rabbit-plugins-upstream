## Description:

Provides an OOMOL oo CLI connector guide for reading Seqera data and launching workflows through a connected Seqera account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Seqera action schemas, read user, workspace, pipeline, and workflow data, and launch Seqera workflows through the OOMOL oo connector when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow launch can change Seqera state and may incur cost.

Mitigation: Require explicit confirmation of the workspace, pipeline, parameters, compute environment, and expected cost before any launch.

Risk: Remote pipe-to-shell installer commands can execute unreviewed code.

Mitigation: Use a trusted, verified oo CLI installation method where possible and review installation steps before running them.

## Reference(s):

- [ClawHub Seqera skill page](https://clawhub.ai/oomol/skills/oo-seqera)
- [Seqera homepage](https://seqera.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Seqera connection setup](https://console.oomol.com/app-connections?provider=seqera)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown instructions with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; workflow launches require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
