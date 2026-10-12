## Description:

Generates a RedNote publishing code from a draft title, text, and images or video so a user can scan it to load the draft in RedNote.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to prepare a RedNote post from supplied copy and media references, then receive a code for loading the draft in the RedNote app.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft content and media references are sent through qhkit to generate the publishing code.

Mitigation: Review the content and obtain user consent before sending it.

Risk: Setup may install or upgrade Node/npm tooling and store a long-lived API token locally.

Mitigation: Prefer a preinstalled, pinned qhkit version and an ephemeral QHKIT_TOKEN instead of persistent configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-publish-code)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown response with publishing-code details and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid calls require user consent; report actual Qinghu credits charged.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
