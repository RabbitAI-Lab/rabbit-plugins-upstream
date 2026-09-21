## Description:

Ecologi lets agents read impact totals and make confirmed Ecologi purchases through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to inspect Ecologi impact totals and, after explicit confirmation, purchase carbon avoidance, carbon removal, habitat restoration, or tree planting through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can ask an agent to run a remote installer script.

Mitigation: Before installing, use a verified oo CLI installation path and avoid piping remote scripts to a shell without review.

Risk: Connected-account write actions can make Ecologi purchases.

Mitigation: Review and explicitly confirm purchase payloads, amounts, attribution, and expected effect before approving write actions.

## Reference(s):

- [ClawHub Ecologi skill page](https://clawhub.ai/oomol/skills/oo-ecologi)
- [Ecologi homepage](https://ecologi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Ecologi purchase actions require exact payload and effect confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
