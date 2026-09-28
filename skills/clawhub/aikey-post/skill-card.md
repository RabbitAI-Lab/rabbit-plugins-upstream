## Description:

Creates WeChat Official Account short-post drafts from validated ideas or fragments, producing a title, a body of up to 1,000 Chinese characters, and a banner image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External knowledge creators use this skill to turn a validated post, topic, or content fragment into a lightweight WeChat Official Account short post with platform-safe wording, draft files, and an optional banner asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated short-post copy or platform compliance edits may be inaccurate or unsuitable for publication.

Mitigation: Review the title, body, and compliance handling before publishing; the skill states that publishing remains the user's responsibility.

Risk: The workflow can write draft files, update topic tracking, copy content to the clipboard, and create banner assets.

Mitigation: Run it only in a workspace where those local side effects are acceptable and inspect the reported paths and clipboard content.

Risk: Banner generation depends on configured image-generation credentials.

Mitigation: Keep credentials in environment configuration, verify the generated banner before use, and fall back to text-only delivery when credentials are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-post)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown draft content with concise chat guidance and optional image-generation command or asset path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local draft files, copy the finished body to the clipboard, and generate a banner image when configured credentials are available.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
