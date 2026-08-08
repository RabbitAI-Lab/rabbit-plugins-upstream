## Description:

Compresses local images, image folders, or remote image URLs through the NX API and returns compression results with CDN URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaowu89](https://clawhub.ai/user/xiaowu89)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to compress JPG, PNG, and WebP images from local paths, folders, or URLs, then review size reductions and CDN links. It is suited to image optimization workflows where sending image contents to the NX API is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image contents are sent to a third-party NX API/CDN.

Mitigation: Use only for images that are approved for third-party processing and avoid sensitive or regulated content unless that transfer is acceptable.

Risk: The skill may read broad .env files and store an NX API key in the current project .env file.

Mitigation: Review the working directory and parent/home .env files before use, and provide credentials through an intentionally scoped environment when possible.

Risk: The skill sends a stable device identifier derived from the machine unless overridden.

Mitigation: Set NX_CLIENT_ID or pass --client with an approved identifier when stable machine-derived identifiers should not be sent.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/xiaowu89/skill-compress)
- [ClawHub skill page](https://clawhub.ai/xiaowu89/skills/skill-compress)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Markdown summary with shell commands and tabular compression results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CDN URLs, compression ratios, original and compressed sizes, API errors, and downloaded files when an output directory is requested.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
