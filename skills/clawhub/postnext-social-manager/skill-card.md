## Description:

Helps agents draft, schedule, publish, and analyze social posts across connected platforms through a PostNext account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postnextio](https://clawhub.ai/user/postnextio)

### License/Terms of Use:

MIT

## Use Case:

Social media managers and teams with a PostNext account use this skill to prepare and publish posts, manage scheduled content and media, and review engagement and audience analytics across connected channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key can act on real connected social accounts.

Mitigation: Use a dedicated key and do not expose it in posts, logs, or URLs.

Risk: Raw curl examples can change public content without the helper's approval gate.

Mitigation: Prefer the bundled helper; require explicit approval of the exact provider, channel, content, media, target, and time before any publish, schedule, cancel, delete, or upload.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/postnextio/skills/postnext-social-manager)
- [Posts and scheduling reference](artifact/references/posts.md)
- [Media uploads reference](artifact/references/media.md)
- [Connected channels reference](artifact/references/channels.md)
- [Analytics reference](artifact/references/analytics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with optional shell commands and account results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include post previews, scheduling outcomes, media URLs, and analytics summaries.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
