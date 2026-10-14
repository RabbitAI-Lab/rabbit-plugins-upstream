## Description:

Publish user-approved static websites to OxyPages and return a live HTTPS link, either temporarily without an account or permanently with an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oxypages](https://clawhub.ai/user/oxypages)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can publish approved static sites for quick previews or permanent hosting and share the resulting HTTPS link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published files become publicly accessible.

Mitigation: Confirm the user requested publication and review the selected files before uploading them.

Risk: An account-owned deployment can replace an existing site's files.

Mitigation: Use an API key only for permanent account-owned sites, confirm the destination, and include all intended files in each deployment.

## Reference(s):

- [OxyPages Publish source repository](https://github.com/oxypages/oxypages-publish)
- [OxyPages Publish on ClawHub](https://clawhub.ai/oxypages/skills/oxypages-publish)
- [OxyPages](https://oxypages.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with HTTPS links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the live URL, expiry and claim link for temporary publishes, and any skipped-file warnings.]

## Skill Version(s):

0.1.0 (source: ClawHub release; embedded skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
