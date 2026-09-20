## Description:

Operates Zip Archive API through an OOMOL-connected account to compress publicly accessible files into ZIP archives and extract publicly accessible archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Zip Archive API through OOMOL for creating ZIP archives from public file URLs and extracting public archives while checking live connector schemas before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archive compression and extraction are presented as read-only, but archive contents and returned transit URLs can contain user data.

Mitigation: Use the skill only with intended public file URLs or archives, confirm inputs before execution, and treat returned transit URLs as sensitive user data.

Risk: The security review notes unverified remote installer commands for the oo CLI.

Mitigation: Prefer verified oo CLI installation steps and review installer commands before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zip-archive-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Zip Archive API homepage](https://archiveapi.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/zip_archive_api.png)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return transit download URLs for generated archives or extracted files.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
