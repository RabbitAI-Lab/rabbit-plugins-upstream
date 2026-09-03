## Description:

Helps a solo knowledge creator turn validated ideas or fragments into a WeChat Official Account short post with a title, concise body, and banner image prompt or asset workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and publishing agents use this skill to convert a validated topic, X-tested post, or content fragment into a lightweight WeChat short post. It guides title handoff, hook checks, domestic-platform compliance review, banner creation, draft saving, clipboard delivery, and follow-up tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can write local draft and banner files, copy text to the clipboard, update a related tracking document, and store writing preferences.

Mitigation: Run it only in a workspace where those side effects are expected, and review reported file paths, clipboard actions, tracking updates, and memory notes before relying on them.

Risk: The banner phase may use configured image-generation credentials and create local image assets.

Mitigation: Keep credentials in environment variables, do not write secrets into files, and fall back to title and body output when image-generation credentials are unavailable.

Risk: The skill applies WeChat domestic-platform content restrictions and may rewrite material that was acceptable on X.

Mitigation: Review the final post for the intended publication venue before posting, especially when adapting X-tested content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-post)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise user-facing instructions, with optional shell commands for image generation and local file operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a WeChat-ready title, body text, banner prompt or image path, draft file path, clipboard status, compliance notes, tracking updates, and scoped memory notes.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
