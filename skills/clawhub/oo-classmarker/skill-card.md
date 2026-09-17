## Description:

ClassMarker connector for searching and reading ClassMarker data through an OOMOL-connected account instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect ClassMarker connector schemas and retrieve accessible ClassMarker groups, links, assigned tests, and recent results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup documents remote shell installers for the oo CLI.

Mitigation: Install the oo CLI from a trusted, verified source instead of allowing an agent to execute curl-to-bash or PowerShell installer commands automatically.

Risk: ClassMarker requests and returned results are processed through OOMOL.

Mitigation: Review the skill before installing and use it only when comfortable routing ClassMarker data through an OOMOL-connected account.

## Reference(s):

- [ClassMarker homepage](https://www.classmarker.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClassMarker skill page](https://clawhub.ai/oomol/skills/oo-classmarker)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include ClassMarker result data returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence, metadata, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
