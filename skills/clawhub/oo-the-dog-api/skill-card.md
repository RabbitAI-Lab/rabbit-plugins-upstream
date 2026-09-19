## Description:

The Dog API skill lets an agent use the OOMOL `oo` CLI to inspect schemas and run The Dog API actions for breed lookup, image retrieval, search, favourites, and votes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate The Dog API through an OOMOL-connected account, including dog breed and image reads plus account favourite and vote workflows. It is intended for tasks where the agent should use the managed connector instead of calling The Dog API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review setup commands before installing and prefer a verified, versioned, signed, or package-manager-based installation method.

Risk: Write and destructive actions can modify favourites or votes in the connected The Dog API account.

Mitigation: Confirm the exact payload, target, and expected effect with the user before create or delete actions.

## Reference(s):

- [The Dog API skill page](https://clawhub.ai/oomol/skills/oo-the-dog-api)
- [The Dog API homepage](https://thedogapi.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the `oo` CLI and return connector responses with data plus execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
