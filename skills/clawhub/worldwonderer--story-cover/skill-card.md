## Description:

Generates genre- and platform-aware Chinese web-novel covers with the book title and author name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Authors and publishing teams use this skill to create illustrated novel covers tailored to a story's genre and target platform, with the book title and pen name included.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local book-setting files and saves covers, prompts, and optional reference-image details to disk.

Mitigation: Review the selected book files and output location before use; avoid including sensitive material in saved prompts or references.

Risk: If the API fallback is used, the title, pen name, prompt, and optional reference image are sent to OpenAI or a configured compatible endpoint.

Mitigation: Use the fallback only when intended, confirm the endpoint, and avoid private reference material unless you consent to its transmission.

## Reference(s):

- [Cover styles and genre guidance](references/cover-styles.md)
- [Image API fallback guide](references/api-fallback.md)
- [Project URL listed in skill metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-cover)

## Skill Output:

**Output Type(s):** [Image files, Text]

**Output Format:** [PNG cover images and plain-text prompt/reference files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Versioned covers avoid overwriting prior images; a platform-sized PNG may also be exported.]

## Skill Version(s):

1.1.12 (source: ClawHub release; bundled frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
