## Description:

Fiber AI helps an agent search and read Fiber AI organization data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Fiber AI organization credits, rate limits, and reference datasets through authenticated OOMOL connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI installation instructions include remote shell and PowerShell installers that could execute arbitrary code if run without verification.

Mitigation: Install the oo CLI manually from a trusted source, prefer signed or checksum-verified packages, and do not allow an agent to run installers or elevated shells automatically.

Risk: Future write or destructive connector actions could change or remove Fiber AI data if used without user review.

Mitigation: Require explicit user confirmation for any action tagged [write] or [destructive], including the exact payload and expected effect.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fiber-ai)
- [Fiber AI Homepage](https://fiber.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schema inspection before each action; current documented actions are read-oriented.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
