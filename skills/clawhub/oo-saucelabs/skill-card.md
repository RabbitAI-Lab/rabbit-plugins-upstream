## Description:

Operate Sauce Labs through OOMOL's oo CLI to read builds and jobs, list job assets, and update virtual-device job metadata with confirmation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to inspect Sauce Labs builds, jobs, and job assets, and to perform controlled virtual-device job updates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that execute directly in a shell.

Mitigation: Review and trust the OOMOL installer source before use, and prefer a pinned, verified installation path for the oo CLI.

Risk: The skill can update Sauce Labs virtual-device job metadata and pass status.

Mitigation: Confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-saucelabs)
- [Sauce Labs Homepage](https://saucelabs.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Sauce Labs connector responses returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
