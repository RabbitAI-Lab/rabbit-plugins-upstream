## Description:

LinkPix helps agents analyze a Douyin or TikTok short-video reference, derive a reusable script structure, adapt it to a user's product, and generate a similarly paced marketing video through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn a provided viral-video link into a reviewed product-specific script and, after explicit confirmation, a generated marketing video. It is intended for lawful adaptation of structure, rhythm, and creative direction rather than direct copying of protected material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product media and reference-video data may be uploaded to an external service.

Mitigation: Use only media the user is authorized to process, avoid sensitive assets unless external processing is acceptable, and disclose the upload before running generation commands.

Risk: The workflow may use or store a qhkit API token.

Mitigation: Use the provided qhkit configuration path or QHKIT_TOKEN environment variable, keep tokens out of chat and logs, and rotate exposed credentials.

Risk: Video generation can spend account credits.

Mitigation: Run an estimate when supported, present the expected credit cost and key parameters, and wait for explicit user approval before submitting generation jobs.

Risk: A viral-video reference can encourage direct copying of protected content.

Mitigation: Adapt only the structure, rhythm, and creative approach; rewrite copy and use the user's own product assets for original marketing work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can produce draft scripts, rewritten scripts, task identifiers, status summaries, generated-video URLs, and credit estimates.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
