## Description:

Cronfree helps agents manage Cronfree schedules through the OOMOL oo CLI, including creating recurring webhook POST schedules and deleting schedules by webhook URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cronfree action schemas and manage recurring webhook schedules from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may install the oo CLI by executing remote installer scripts directly.

Mitigation: Review the installer path first and prefer a verified release or documented package-manager installation flow.

Risk: The skill can create schedules and delete schedules associated with webhook URLs.

Mitigation: Confirm the exact payload, action effect, and target webhook URL before allowing write or destructive actions.

## Reference(s):

- [Cronfree homepage](https://cronfree.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
