## Description:

Helps a solo knowledge creator turn validated ideas or fragments into a WeChat public-account short post with a title, concise body, and banner image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use this skill to prepare lightweight WeChat public-account posts from already validated content, including a title of 20 or fewer Chinese characters, body text of 1000 or fewer Chinese characters, and a banner image direction or asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local reference and memory files and may save drafts, generated banners, and style-feedback memory under the user's vault.

Mitigation: Install and run it only where those local reads and writes are acceptable, and review generated drafts and remembered feedback before reuse.

Risk: The skill may copy final post text to the clipboard for use in the WeChat editor.

Mitigation: Review the clipboard content before pasting or publishing, especially for compliance-sensitive public-platform wording.

Risk: The skill can update a related topic pipeline when content comes from a validated X post.

Mitigation: Check pipeline updates after use if the source content should not be marked as converted to a WeChat short post.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-post)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown draft with plain-text title/body, banner-image prompt or file path, and concise handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected post output includes one title, one short body, and one banner image; publication remains user-controlled.]

## Skill Version(s):

0.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
