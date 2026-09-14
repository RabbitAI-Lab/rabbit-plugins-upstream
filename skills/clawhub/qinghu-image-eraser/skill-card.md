## Description:

Guides an agent to use Qinghu AI's qhkit CLI to erase watermarks, text, people, and unwanted objects from product images while filling the background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to clean product images by removing specified watermarks, text, people, or clutter and returning generated image URLs from Qinghu AI. It also guides setup, model and size option checks, credit estimation, and failure handling for qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI package with local execution and upgrade behavior.

Mitigation: Install @iqinghu/qhkit only when the package and Qinghu service are trusted; prefer a pinned, local, sandboxed installation and independently verify upgrade commands before running them.

Risk: Selected image files may be uploaded to the Qinghu service for generation.

Mitigation: Use only images approved for that service and confirm that privacy, rights, and customer-data handling requirements allow upload.

Risk: The workflow requires an API token for Qinghu access.

Mitigation: Store the token in a managed secret or environment variable, avoid placing it in prompts or logs, and rotate it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-eraser)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide qhkit option lookup, credit estimation, image generation, and delivery of returned image URLs with actual credit usage.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
