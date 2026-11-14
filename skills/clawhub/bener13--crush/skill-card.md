## Description:

Builds a local AI simulation profile from chat logs, photos, and social media, with Bayesian memory tagging, attachment-style analysis, and generated skill files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bener13](https://clawhub.ai/user/bener13)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use XB to create local crush profiles from personal chat logs, photos, and social posts, then generate diagnostic reports, conversation-practice simulations, and updateable skill files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles intimate third-party chats, photos, and social media that may involve privacy or consent concerns.

Mitigation: Process only data you have rights and consent to use, keep artifacts local, and delete source material and generated profiles when no longer needed.

Risk: Screenshot parsing can upload images through an API path despite local-only privacy claims.

Mitigation: Use offline OCR mode for sensitive screenshots, or review and disable API-based screenshot extraction before processing private material.

Risk: Generated persona skills can support deceptive impersonation of a real person.

Mitigation: Label generated profiles as AI simulations, avoid presenting simulated text as the real person's speech, and review generated skill files before use.

Risk: Profile file operations can affect local files if slugs or output paths are not constrained.

Mitigation: Validate profile slugs, restrict output to the intended profile directory, review delete and rollback commands before execution, and keep backups.

Risk: Photo EXIF analysis can expose precise GPS coordinates or routine patterns.

Mitigation: Strip or avoid GPS EXIF data unless needed, and remove precise location or routine details from generated profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bener13/skills/crush)
- [Publisher profile](https://clawhub.ai/user/bener13)
- [Declared project homepage](https://github.com/NatalieCao323/crush-skill)
- [OpenClaw](https://openclaw.ai)
- [Python](https://python.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, generated skill files, Python tool outputs, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local profile artifacts under crushes/{slug}/ when enabled by the agent.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
