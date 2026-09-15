## Description:

Fluxguard lets an agent operate Fluxguard through the OOMOL-connected oo CLI to read, create, update, and delete monitored pages, categories, sites, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Fluxguard resources from an agent through OOMOL's connected CLI. It supports inspecting live action schemas, reading account and monitoring data, and carrying out confirmed write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Install the oo CLI only from a verified OOMOL release or documented package source, and review installer commands before execution.

Risk: Write actions can change Fluxguard pages, categories, webhooks, or crawl state.

Mitigation: Fetch the live action schema, present the exact payload and expected effect, and get user confirmation before running write actions.

Risk: Destructive actions can delete Fluxguard pages, sites, webhooks, or associated data.

Mitigation: Confirm the target resource and get explicit approval before running destructive actions.

## Reference(s):

- [ClawHub Fluxguard skill page](https://clawhub.ai/oomol/skills/oo-fluxguard)
- [Fluxguard homepage](https://fluxguard.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Fluxguard account; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence.json release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
