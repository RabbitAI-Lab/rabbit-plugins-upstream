## Description:

Enables agents to operate Baidu Netdisk through the OOMOL baidu_netdisk connector for reading, creating, searching, and updating files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they want an agent to inspect account details, list or search Baidu Netdisk files, and perform confirmed create, copy, move, rename, or upload actions through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Baidu Netdisk contents by creating, copying, moving, renaming, or uploading files.

Mitigation: Review the exact connector action and JSON payload before approving any state-changing operation.

Risk: First-time setup or expired credentials can block connector actions.

Mitigation: Run authentication or connection setup only after an oo CLI command fails with a matching auth or connection error.

## Reference(s):

- [Baidu Netdisk homepage](https://pan.baidu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands and JSON request payloads for Baidu Netdisk connector actions.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
