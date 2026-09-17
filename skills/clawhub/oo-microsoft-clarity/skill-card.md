## Description:

Microsoft Clarity (clarity.microsoft.com). Use this skill for ANY Microsoft Clarity request - searching and reading data. Whenever a task involves Microsoft Clarity, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Microsoft Clarity connector schemas and export recent live insights through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that can execute code from external URLs.

Mitigation: Use a pinned, signed, or manually reviewed installation path and avoid running remote installers until the source and contents have been independently verified.

Risk: The skill accesses Microsoft Clarity through OOMOL as an intermediary.

Mitigation: Install only if the user is comfortable routing Microsoft Clarity data through OOMOL-connected services.

Risk: Shell-interpolated JSON payloads can be malformed or unsafe when values contain quotes or shell metacharacters.

Mitigation: For dynamic payloads, write JSON to a file and pass it with --data @path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-microsoft-clarity)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Microsoft Clarity homepage](https://clarity.microsoft.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Microsoft Clarity icon](https://static.oomol.com/logo/third-party/microsoft_clarity.png)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
