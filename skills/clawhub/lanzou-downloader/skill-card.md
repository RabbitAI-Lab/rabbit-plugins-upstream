## Description:

Helps agents list and download files from Lanzou share links, including password-protected links and selected batch downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwqww1](https://clawhub.ai/user/wwqww1)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can inspect Lanzou share links, choose files from a numbered listing, and download individual files or batches to a chosen location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote pages can supply JavaScript that the skill executes.

Mitigation: Review the skill before installing; use only trusted share links and avoid running it in a workspace containing secrets.

Risk: The documented Lanzou-only network boundary is not enforced, so links or redirects may reach other destinations.

Mitigation: Avoid providing share passwords unless the implementation restricts destinations to Lanzou-only HTTPS and removes remote JavaScript execution.

Risk: The optional insecure mode disables TLS certificate checks.

Mitigation: Keep certificate verification enabled; avoid the insecure option unless you accept the interception risk.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wwqww1/skills/lanzou-downloader)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance, JSON file listings and manifests, and downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports numbered selection, batch downloads, and password-protected shares.]

## Skill Version(s):

0.0.9 (source: ClawHub release; embedded files identify 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
