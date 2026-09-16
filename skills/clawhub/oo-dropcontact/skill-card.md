## Description:

Use Dropcontact through an OOMOL-connected account to inspect action schemas, submit contact enrichment requests, and retrieve enrichment results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Dropcontact from an agent through the OOMOL oo CLI. It supports retrieving enrichment results and submitting up to 250 contacts for asynchronous email verification and enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can lead users to execute remote installer scripts directly.

Mitigation: Review setup before installing; prefer a signed or verifiable oo CLI installation method, or inspect the installer before running it.

Risk: The submit_enrichment action can send contact data to Dropcontact through OOMOL.

Mitigation: Confirm the exact payload and effect with the user before running submit_enrichment, and avoid sending unnecessary personal data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dropcontact)
- [Dropcontact homepage](https://www.dropcontact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples; connector action output is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Dropcontact account; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
