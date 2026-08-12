## Description:

Generates and edits images, short videos, animated images, and talking avatars through a user-configured Kandinsky API instance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gen-ai-team](https://clawhub.ai/user/gen-ai-team)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or modify visual media through Kandinsky, including text-to-image, image editing, upscaling, short video generation, image animation, and talking avatar workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, input images, and audio are sent to the configured Kandinsky API instance with the user API key.

Mitigation: Install and use the skill only with a trusted Kandinsky API instance, keep the key private, and prefer HTTPS or private/loopback API addresses.

Risk: Plain HTTP to an untrusted public address can expose the API key in transit.

Mitigation: Use HTTPS or a private/loopback API address; enable insecure transport only deliberately after reviewing the exposure.

Risk: Disabling content filtering can increase misuse and policy risk for generated or edited media.

Mitigation: Leave content filtering enabled unless there is a deliberate, reviewed reason to change it.

## Reference(s):

- [Kandinsky API cheatsheet](references/api-cheatsheet.md)
- [Kandinsky prompting guide](references/prompting.md)
- [ClawHub skill page](https://clawhub.ai/gen-ai-team/skills/kandinsky-skill)
- [Publisher profile](https://clawhub.ai/user/gen-ai-team)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and saved media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to call a Python script that saves generated or edited media files and reports the final path.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
