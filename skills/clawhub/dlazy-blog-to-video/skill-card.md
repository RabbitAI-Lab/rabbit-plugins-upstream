## Description:

blog to video, blog post to video, article to video — convert a blog post into a narrated video with storyboard, voiceover, and build. Use when the user gives a blog post (text or link) and wants a video version for social or YouTube.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to turn blog posts or other documents into narrated videos for social media, YouTube, explainers, reports, courses, or training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy; attached files are uploaded to its media storage.

Mitigation: Use only content you are comfortable sending to dLazy, and avoid uploading sensitive material.

Risk: The CLI stores an organization API key in its local configuration by default.

Mitigation: Use the DLAZY_API_KEY environment-variable option when preferred, protect the local config, and rotate or revoke keys from the organization dashboard when needed.

Risk: Hosted video generation may incur account costs.

Mitigation: Check generation costs and available credits before starting work.

Risk: The external CLI executable and hosted service were not audited in the supplied security evidence.

Mitigation: Review the pinned CLI package before installing it.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Markdown]

**Output Format:** [Narrated video with storyboard and voiceover, with conversational text and Markdown project guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted workflow can upload attached files and returns video-generation results.]

## Skill Version(s):

1.0.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
