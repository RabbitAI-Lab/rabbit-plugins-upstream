## Description:

Creates novel-cover prompts and, when requested, generates cover images in a selected genre and platform-ready format.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Authors and writers use this skill to develop illustrated novel-cover prompts from a book's title and genre, then optionally generate and prepare a cover image for a publishing platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, book details, or reference images may contain sensitive information shared with the selected image-generation provider.

Mitigation: Review the provider and avoid submitting sensitive material unless its handling is appropriate.

Risk: The security scan was partial because a local path-like reference could not be resolved, leaving evidence incomplete.

Mitigation: Review the affected reference and complete a full security scan before relying on the verdict.

## Reference(s):

- [Cover style and platform guidance](references/cover-styles.md)
- [Image generation API fallback guidance](references/api-fallback.md)
- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-cover)
- [Repository link listed in skill metadata (provenance unavailable)](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Text, Image files, Guidance]

**Output Format:** [Complete image prompts, optional PNG cover images, and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only or image-generation workflow; portrait cover ratios, with platform-sized export when requested.]

## Skill Version(s):

1.1.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
