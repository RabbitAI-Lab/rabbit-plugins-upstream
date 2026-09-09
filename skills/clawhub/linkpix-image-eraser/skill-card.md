## Description:

This skill helps agents use LinkPix through qhkit to erase watermarks, text, people, and unwanted objects from product images, then regenerate the edited background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through product-image cleanup tasks such as removing watermarks, text, people, or other unwanted objects while preserving and filling the surrounding image background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external @iqinghu/qhkit npm package and LinkPix service.

Mitigation: Install only when those dependencies are trusted; prefer a pinned, reviewed qhkit version in an isolated environment.

Risk: Install and upgrade guidance can lead to mutable external command execution.

Mitigation: Review package names, versions, registries, and any suggested upgrade commands before running them.

Risk: Image editing may expose sensitive images or service tokens to the external service.

Mitigation: Avoid providing sensitive images or tokens beyond what the specific task requires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON payloads, Image URLs]

**Output Format:** [Markdown guidance with bash commands and JSON CLI payloads; generated image results are returned as URLs by qhkit.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the qhkit CLI and a LinkPix token; generated image output should be visually checked for natural background completion and unchanged product details.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
