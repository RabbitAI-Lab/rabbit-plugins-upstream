## Description:

Read Lanhu UI designs, extract slices, and download Web/iOS/Android assets using lh-design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuwenxindeai](https://clawhub.ai/user/xuwenxindeai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to inspect Lanhu design slices and generate platform-specific asset download commands for Web, iOS, and Android.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lanhu cookies may grant access to private design assets.

Mitigation: Treat LANHU_COOKIE and DDS_COOKIE as session credentials, prefer a scoped Lanhu account or session, and avoid storing cookies in shared workspaces.

Risk: The workflow depends on the external lh-design CLI.

Mitigation: Install lh-design only when the upstream project is trusted, then verify the installed command with lh-design --help before using the skill.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and generated asset files from the external CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Lanhu URL, LANHU_COOKIE, and optionally DDS_COOKIE.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
