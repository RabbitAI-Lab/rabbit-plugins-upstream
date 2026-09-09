## Description:

Generates multiple POD print design variations from a source pattern with LinkPix and qhkit, varying colorways, style, elements, and arrangement while preserving the source theme.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, POD sellers, and agents use this skill to create a coordinated set of print-pattern variants from one input image for ecommerce product design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned third-party qhkit CLI globally.

Mitigation: Review the package before installation and prefer a pinned or platform-managed install path.

Risk: The skill requires a LinkPix API token for CLI access.

Mitigation: Provide the token through a protected secret store or environment variable rather than a visible command line.

Risk: Generated pattern variations may differ from source details.

Mitigation: Review generated images for required motifs, style, and production constraints before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and qhkit JSON parameters; generated image URLs are relayed from the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the qhkit CLI, a LinkPix API token, local or URL image inputs, and sufficient service credits for image generation.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
