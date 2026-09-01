## Description:

Creates a WeChat Official Account short post from validated content or fragments, producing a short title, concise body text, and a banner image concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to turn an already validated idea, topic, or content fragment into a lightweight WeChat public-account post with platform-compliant wording and a banner direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create local draft files and banner images in configured vault paths.

Mitigation: Confirm the target vault paths before use and review generated files before publishing or sharing.

Risk: The skill may copy generated body text to the clipboard.

Mitigation: Review clipboard contents before pasting into a public editor or replacing existing clipboard data.

Risk: The skill may call a configured image-generation provider for banner creation.

Mitigation: Confirm image-generation credentials and provider settings are configured appropriately, and use the text-only fallback if they are unavailable.

Risk: The skill may write scoped memory entries about style preferences and successful title/banner patterns.

Mitigation: Keep memory locations scoped to this workflow and avoid storing sensitive personal or business information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-post)
- [ClawHub publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional shell commands and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create a local draft file, copy body text to the clipboard, generate or request a banner image, and record scoped style memory when configured.]

## Skill Version(s):

0.2.1 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
