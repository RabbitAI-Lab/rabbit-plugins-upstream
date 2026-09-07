## Description:

Deploy an HTML page to the internet and return a public URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiantoucn](https://clawhub.ai/user/jiantoucn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to upload a user-selected HTML file or supported site archive to Dropage and return a public URL with expiry and optional visit limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The uploaded file or archive becomes publicly reachable through the returned Dropage URL.

Mitigation: Review the selected file or archive before upload and deploy only content intended for public access.

Risk: Private, internal, proprietary, or credential-containing content could be exposed if selected for deployment.

Mitigation: Do not upload sensitive files; inspect archives for embedded secrets, private data, and unintended assets before running the upload command.

Risk: A longer expiry or unlimited visit setting can keep public access available longer than intended.

Mitigation: Confirm the requested expiry and visit limit before deployment, especially for 7-day or 14-day uploads.

## Reference(s):

- [Dropage upload API](https://dropage.online/api/upload)
- [Dropage deploy skill update URL](https://dropage.online/dropage-deploy.md)
- [ClawHub skill page](https://clawhub.ai/jiantoucn/skills/dropage-deploy)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and parsed JSON response details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a public URL, expiration time, and visit limit on successful upload; reports server error details on failure.]

## Skill Version(s):

1.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
