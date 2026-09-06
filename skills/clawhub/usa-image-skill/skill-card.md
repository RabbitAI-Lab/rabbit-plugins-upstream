## Description:

USA零生图技能 uses usa0.top's OpenAI-compatible Images API to generate or edit images from prompts and local or remote reference images, with setup guidance for USA_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tkxs](https://clawhub.ai/user/tkxs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate new images or edit supplied reference images through usa0.top, including configuring the required image-generation API key and selecting image parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, and the configured API key are sent to usa0.top during generation or editing.

Mitigation: Use the skill only with content appropriate for that service, avoid sensitive prompts or images, and use a dedicated, revocable, spending-limited API key.

Risk: A custom --base-url destination would receive the bearer API key.

Mitigation: Use --base-url only when the destination is fully trusted.

Risk: Passing --api-key on the command line can expose the key through shell history or process metadata.

Mitigation: Prefer USA_API_KEY or the Windows configuration window, and avoid placing real keys in chat or command history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tkxs/skills/usa-image-skill)
- [usa0.top](https://usa0.top)
- [usa0.top API documentation](https://usa0.top/docs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved to a local output directory; the script prints MEDIA lines for produced files.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
