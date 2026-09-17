## Description:

L2S helps agents read, create, and update L2S shortened URL data through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage L2S shortened URLs from an agent session, including looking up existing links, creating new shortened URLs, and updating link details after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote shell installer commands.

Mitigation: Review the oo CLI installer source or use a verified vendor installation path before installing.

Risk: Shorten and update actions change L2S account data.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [L2S homepage](https://www.l2s.is)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [L2S ClawHub skill page](https://clawhub.ai/oomol/skills/oo-l2s)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
