## Description:

Sif helps agents search and read Sif data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route Sif requests through an OOMOL-connected account, inspect live Sif action schemas, and run Amazon market, keyword, and ASIN analysis actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-analysis requests send relevant ASIN, keyword, or business query data to Sif/OOMOL.

Mitigation: Review payloads before execution and avoid sending sensitive or unnecessary business data.

Risk: Many market-analysis actions consume Sif points.

Mitigation: Check the documented point cost for the selected action and confirm costly requests before running them.

Risk: Future Sif actions tagged as write or destructive could change or remove Sif data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running any write or destructive action.

## Reference(s):

- [Sif homepage](https://www.sif.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Sif skill listing](https://clawhub.ai/oomol/skills/oo-sif)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live schema inspection steps before constructing connector payloads.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
