## Description:

here.now lets agents publish websites and files to live URLs and manage private Drive storage for persistent agent files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to publish static sites, single files, workspace-owned sites, and selected Drive snapshots to here.now. They can also store, retrieve, share, and manage private files through here.now Drive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published sites can make selected content externally reachable.

Mitigation: Review files before publishing, avoid uploading secrets, and use password, restricted access, or private Drive storage for private material.

Risk: Long-lived account credentials may be retained for future here.now operations.

Mitigation: Store credentials with restrictive permissions only when persistence is intended, and revoke or remove ~/.herenow/credentials when account access should no longer be available.

Risk: Drive share tokens can grant another agent access to private files.

Mitigation: Use scoped Drive tokens with a narrow path prefix and short TTL, then revoke tokens that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)
- [here.now documentation](https://here.now/docs)
- [here.now OpenAPI schema](https://here.now/openapi.json)
- [here.now access control documentation](https://here.now/docs#access-control)
- [here.now workspace documentation](https://here.now/docs#workspaces)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and script or API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce live site URLs, Drive share blocks, and local credential or state files when used.]

## Skill Version(s):

1.25.0 (source: evidence.json release.version and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
