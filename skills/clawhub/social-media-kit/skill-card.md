## Description:

Generate a complete week of platform-optimized social media posts, posting recommendations, hashtag suggestions, JSON export, and an HTML content calendar from a single topic or brand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, agencies, founders, creators, and startups use this skill to draft multi-platform social media calendars and export planning files for scheduling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML calendars from untrusted JSON may include calendar metadata fields that are not consistently HTML-escaped.

Mitigation: Open generated calendars only from trusted inputs or review/sanitize imported JSON before rendering HTML.

Risk: The skill writes JSON and HTML files to the filesystem.

Mitigation: Use an output directory you control and review generated files before sharing or importing them into scheduling tools.

## Reference(s):

- [Content Strategy](references/content-strategy.md)
- [Platform Guide](references/platform-guide.md)
- [Source Repository](https://github.com/voronindenis5/social-media-kit)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/social-media-kit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Console text, structured JSON files, and HTML calendar files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes content.json and calendar.html to a user-selected output directory; can also render an HTML calendar from an existing JSON export.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
