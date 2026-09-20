## Description:

Apiframe helps agents operate Apiframe through an OOMOL-connected account for schema inspection, generation job submission, job lookup, job listing, and model discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent run Apiframe operations through OOMOL, including inspecting live schemas, submitting image, music, and video generation jobs, listing models or jobs, and checking job status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell installer commands.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI from trusted official documentation and verify the installer where possible.

Risk: Apiframe generation actions may consume credits or create account state.

Mitigation: Confirm the exact generation payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Apiframe skill page](https://clawhub.ai/oomol/skills/oo-apiframe)
- [Apiframe homepage](https://apiframe.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; write actions should be confirmed because they can consume credits or create account state.]

## Skill Version(s):

1.0.1 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
