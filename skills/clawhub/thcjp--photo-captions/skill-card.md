## Description:

Generates differentiated social media captions for photography work across Instagram, Flickr, X, Glass, Reddit, and other platforms by adapting tone, format, tags, and equipment details to each community.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External photographers, creators, social media managers, and editorial teams use this skill to turn photo context into platform-specific captions for publishing across multiple photography and social communities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags broad read, write, and shell authority that is wider than the visible caption-writing task requires.

Mitigation: Install only in workspaces where broad file and shell access is acceptable, and grant the minimum tools needed for caption generation.

Risk: Photo inputs, captions, API keys, and workspace files may contain sensitive or private information.

Mitigation: Avoid using sensitive photos or secrets with this skill, and scope any required API key narrowly.

Risk: Captions may overstate unknown details if the photo location, equipment, subject, or publication context is incomplete.

Mitigation: Review generated captions before posting and provide only verified location, equipment, and subject details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/photo-captions)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown sections with platform-specific caption text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces up to 12 platform-specific caption variants and may include titles, hashtags, equipment lines, topics, or comment text depending on the target platform.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
