## Description:

Guides an agent through Qinghu AI's women's viral-video imitation workflow, using one reference video and one model reference image to transfer the video's motion to a new real or virtual model for short-form apparel content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to prepare, quote, submit, monitor, and deliver Qinghu AI women's apparel short-video imitation jobs from authorized reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade Node/npm tooling and write qhkit configuration.

Mitigation: Run it in a sandbox or use a preinstalled qhkit environment, and approve package or runtime changes before allowing them on a shared system.

Risk: The workflow uses Qinghu credentials and can spend Qinghu credits when generation is submitted.

Mitigation: Use a scoped or low-value token where possible, run the estimate step first, and require explicit user confirmation before generate.

Risk: Reference videos, model images, and likenesses may create copyright, publicity, or authorization issues.

Mitigation: Use only owned or properly licensed source media and obtain permission for any identifiable person's likeness before commercial use.

Risk: The documented workflow fields are a snapshot and the live Qinghu workflow can change.

Mitigation: Run qhkit workflow options before preparing parameters and use the returned field labels exactly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit workflow parameters, quote and status guidance, final media URLs, and a final Qinghu credit-consumption line when a task succeeds.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
