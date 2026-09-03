## Description:

aggclaw helps agents query AppGrowing Global to find, analyze, and summarize global ad creatives, including game, non-game, and Inspire ideation modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and growth teams use this skill to ask an agent for AppGrowing Global ad creative analysis and ideation. The skill can continue analysis sessions and download user-selected creative materials from the active session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ad-analysis prompts to AppGrowing/YouCloud using the configured YOUCLOUD_API_KEY.

Mitigation: Install only when that external API use is acceptable, configure the key explicitly, and avoid submitting prompts that should not be shared with the service.

Risk: User-requested creative downloads can save media files locally, including all creatives in a session if that scope is chosen.

Mitigation: Review the download scope before choosing all creatives and prefer mentioned-creatives-only downloads when that is sufficient.

## Reference(s):

- [aggclaw ClawHub Skill Page](https://clawhub.ai/youcloud/skills/aggclaw)
- [AppGrowing](https://appgrowing.net/)
- [Usage Examples](references/example.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown analysis text with optional local downloaded media files and setup commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires YOUCLOUD_API_KEY; can preserve session_id for follow-up analysis and save requested creative downloads locally.]

## Skill Version(s):

1.2.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
