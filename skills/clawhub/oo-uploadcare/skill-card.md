## Description:

Uploadcare is a skill for handling Uploadcare requests, including reading, creating, updating, and deleting data through the OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Uploadcare files, groups, and project information through the oo CLI using an OOMOL-connected Uploadcare account. It supports read operations, permanent file storage, and destructive file deletion with explicit confirmation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that are not pinned or independently verified.

Mitigation: Install the oo CLI only from a verified package or pinned release, and verify checksums or signatures before running installer scripts.

Risk: The skill can perform write and destructive Uploadcare actions, including permanent storage changes and file deletion.

Mitigation: Confirm the exact action, target UUID or payload, and expected effect with the user before allowing write or destructive commands to run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-uploadcare)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Uploadcare Homepage](https://uploadcare.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should inspect the live connector schema before constructing action payloads and should preserve execution IDs returned under meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
