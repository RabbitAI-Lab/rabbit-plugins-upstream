## Description:

詹明明·公众号短文 helps a content creator turn validated notes or fragments into a WeChat Official Account short post with a title, concise body, and banner-image direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators use this skill to convert validated ideas, X-tested posts, topic notes, or short fragments into lightweight WeChat Official Account posts. It guides title handoff, short-form body drafting, platform-compliance review, banner image prompting, draft saving, and clipboard handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local zmm reference and memory files as part of its drafting workflow.

Mitigation: Use it only in workspaces where those files are intended for the agent to access, and review generated drafts before reuse.

Risk: The skill may save local drafts and banner images and copy finished text to the clipboard.

Mitigation: Check saved paths and clipboard contents before pasting into a publishing tool or sharing externally.

Risk: The skill can optionally update a related X-testing pipeline note.

Mitigation: Review any pipeline-note changes before committing, syncing, or relying on them for publication tracking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-post)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with drafted post text, metadata, file paths, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a WeChat short-post draft, banner image prompt or generated image path, local draft path, clipboard handoff notice, and related workflow guidance.]

## Skill Version(s):

0.2.4 (source: server release metadata; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
