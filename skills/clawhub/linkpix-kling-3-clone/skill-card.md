## Description:

Helps short-video creators adapt a reference video's shot structure into a product-focused Kling 3.0 script and generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video marketers, editors, and online sellers use this skill to analyze a reference clip, adapt its pacing and shot structure to their product, and request a Kling 3.0 video after approving the script and estimated cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup can install unpinned remote packages and change the user's environment.

Mitigation: Prefer a preinstalled or pinned qhkit version; review package installation, PATH changes, and shell-profile edits before allowing them.

Risk: The workflow handles a qhkit API key.

Mitigation: Use a secure credential channel or environment variable and avoid exposing the key in chat, logs, or shared shell history.

## Reference(s):

- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with a script comparison, command guidance, and a link to the generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a reference image and explicit user approval of the parameters and estimated credits.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
