## Description:

CloudConvert lets agents read, create, update, and delete CloudConvert data through OOMOL's oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage CloudConvert jobs and tasks through an OOMOL-connected account, including URL-based conversions, job inspection, retries, cancellation, deletion, and credit lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands executed directly in a shell.

Mitigation: Review the oo CLI installation path before use and prefer verified official installers or package-manager steps instead of piping remote scripts into a shell.

Risk: Write and destructive CloudConvert actions can consume credits or delete jobs, tasks, and related data.

Mitigation: Confirm the exact payload and target with the user before any write or destructive action.

## Reference(s):

- [CloudConvert homepage](https://cloudconvert.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [CloudConvert skill on ClawHub](https://clawhub.ai/oomol/skills/oo-cloudconvert)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live connector schemas before running CloudConvert actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
