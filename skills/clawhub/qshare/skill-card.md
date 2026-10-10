## Description:

Share one local file through a temporary TryCloudflare URL or, with explicit confirmation, upload it to the qshare CNB release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[steinvenic](https://clawhub.ai/user/steinvenic)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents sharing a local file use qshare to provide a temporary public download link and QR code, or, with explicit confirmation, a persistent CNB download link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing one file may expose neighboring local files through the public URL.

Mitigation: Do not use this version for sensitive directories; verify file isolation before sharing.

Risk: The CNB upload option ships a hardcoded remote upload credential.

Mitigation: Avoid CNB uploads until the credential is removed and uploads use user-owned or scoped authorization.

Risk: Public download links have no access control; CNB uploads are not automatically deleted.

Mitigation: Encrypt private files before sharing, confirm CNB uploads explicitly, and remove uploaded files when no longer needed.

## Reference(s):

- [qshare source repository (server-resolved provenance)](https://github.com/steinvenic/qshare)
- [Cloudflared releases](https://github.com/cloudflare/cloudflared/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and a public download URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a QR code for the temporary share; CNB links persist until separately removed.]

## Skill Version(s):

0.1.0 (source: ClawHub release; bundled package version: 0.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
