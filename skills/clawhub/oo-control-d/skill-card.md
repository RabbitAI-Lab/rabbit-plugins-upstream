## Description:

Control D (controld.com) helps agents read, create, update, and delete Control D data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Control D connector schemas and manage profiles, DNS rules, service categories, services, and current API-detected IP details through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands are present in setup guidance, and security evidence warns against automatic execution of those commands.

Mitigation: Install the OOMOL CLI through a trusted, verified method and do not allow an agent to run remote installer commands automatically.

Risk: The skill can create, replace, or delete Control D DNS rules.

Mitigation: Confirm exact write or delete payloads and effects with the user before executing tagged write or destructive actions.

## Reference(s):

- [Control D homepage](https://controld.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Control D skill on ClawHub](https://clawhub.ai/oomol/skills/oo-control-d)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses with data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: server evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
