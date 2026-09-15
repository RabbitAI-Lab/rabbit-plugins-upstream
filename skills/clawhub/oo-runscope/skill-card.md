## Description:

Runscope (blazemeter.com). Use this skill for ANY Runscope request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Runscope API Monitoring account, bucket, test, environment, and result data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands for the oo CLI.

Mitigation: Install the CLI from a trusted, versioned source with verification instead of piping a remote script directly into a shell.

Risk: The skill accesses Runscope data through an OOMOL-connected account.

Mitigation: Connect the Runscope account only when OOMOL-mediated read access to that data is intended.

## Reference(s):

- [Runscope on ClawHub](https://clawhub.ai/oomol/skills/oo-runscope)
- [Runscope API Monitoring](https://www.blazemeter.com/api-monitoring)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to inspect live connector schemas before making read-only Runscope requests.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
