## Description:

Cuttly helps agents operate Cuttly through an OOMOL-connected account to shorten URLs, retrieve click analytics, and inspect action schemas before submitting payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Cuttly actions through the OOMOL oo CLI, including creating short URLs and retrieving click analytics from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill under-labels URL creation: shorten_url creates a Cuttly short URL but is not marked as a write action in the available actions list.

Mitigation: Require explicit confirmation of the destination URL and expected account change before running shorten_url.

Risk: The security evidence flags pipe-to-shell installer commands for the OOMOL CLI as unsafe unless independently trusted and verified.

Mitigation: Prefer an already installed oo CLI or the documented install guide, and verify the installer source before running remote installer commands.

## Reference(s):

- [Cuttly ClawHub listing](https://clawhub.ai/oomol/skills/oo-cutt-ly)
- [Cuttly homepage](https://cutt.ly)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke OOMOL-connected Cuttly actions through the oo CLI and return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
