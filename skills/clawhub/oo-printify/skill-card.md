## Description:

Use this skill for Printify requests to read, create, and update Printify data through the OOMOL-connected oo CLI instead of calling the Printify API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Printify shop data through an OOMOL-connected account, including retrieving shops, orders, and products and constructing connector payloads from live schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs the agent to run remote installer scripts for the oo CLI.

Mitigation: Review the installer before use, prefer a verified package or checksum/signature review, and avoid running curl|bash or irm|iex blindly.

Risk: The skill can read Printify shop, product, and order data through the connected OOMOL account.

Mitigation: Use it only with an authorized Printify connection and confirm the intended shop or account scope before retrieving sensitive business data.

Risk: Actions tagged as write or destructive may change Printify state if invoked with the wrong payload.

Mitigation: Fetch the live schema, confirm the exact target, payload, and expected effect with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [Printify homepage](https://printify.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Printify skill page](https://clawhub.ai/oomol/skills/oo-printify)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects live connector schemas to be checked before payloads are built.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
