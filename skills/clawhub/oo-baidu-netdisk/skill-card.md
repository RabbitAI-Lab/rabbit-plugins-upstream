## Description:

Baidu Netdisk lets agents read, create, update, search, and delete data in a connected Baidu Netdisk account through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Baidu Netdisk account from an agent, including browsing, search, metadata and quota checks, and confirmed file-management actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Baidu Netdisk account and app-directory data through OOMOL-connected credentials.

Mitigation: Confirm the user is comfortable connecting Baidu Netdisk through OOMOL and treat read actions as account or app-directory access.

Risk: Write actions can create, copy, move, rename, or upload files and folders.

Mitigation: Check the exact target and payload with the user before approving any write operation.

Risk: The delete action can remove files or folders.

Mitigation: Require explicit user approval for the target and effect before running destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-baidu-netdisk)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Baidu Netdisk homepage](https://pan.baidu.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs connector actions with JSON payloads and returns connector JSON responses that include data and an execution id.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
