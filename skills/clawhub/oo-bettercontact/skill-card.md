## Description:

BetterContact (bettercontact.rocks). Use this skill for BetterContact requests such as reading account balances, retrieving enrichment results, and submitting leads through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BetterContact through OOMOL, including checking credits, retrieving enrichment results, and submitting lead enrichment requests after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the OOMOL CLI.

Mitigation: Independently verify the OOMOL CLI installer and prefer reviewed installation steps before running curl-to-bash or PowerShell iex commands.

Risk: submit_enrichment sends lead data to the BetterContact connector and may consume account credits.

Mitigation: Confirm the exact payload and intended effect with the user before submitting enrichment requests.

## Reference(s):

- [BetterContact homepage](https://bettercontact.rocks)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [BetterContact skill page](https://clawhub.ai/oomol/skills/oo-bettercontact)
- [BetterContact icon](https://static.oomol.com/logo/third-party/bettercontact.svg)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns JSON connector responses when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
