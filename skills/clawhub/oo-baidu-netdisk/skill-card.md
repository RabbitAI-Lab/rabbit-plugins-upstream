## Description:

Baidu Netdisk lets an agent read, create, and update Baidu Netdisk data through the OOMOL baidu_netdisk connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Baidu Netdisk through an OOMOL-connected account, including account and quota lookup, file listing, file search, downloads, uploads, folder creation, moves, renames, copies, text-file creation, and share-link creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read cloud-file metadata and content through Baidu Netdisk.

Mitigation: Install it only when the user intends Codex to operate Baidu Netdisk through OOMOL, and keep account connection steps intentional.

Risk: Write and share-link actions can change files, folders, or access to content.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for any destructive operation.

Risk: First-time CLI installation, OOMOL login, or connection setup affects the user's local or cloud account state.

Mitigation: Run setup steps only after an auth, connection, or missing-command failure and only with deliberate user authorization.

## Reference(s):

- [Baidu Netdisk homepage](https://pan.baidu.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Baidu Netdisk skill on ClawHub](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
