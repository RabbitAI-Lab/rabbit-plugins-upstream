## Description:

Retrieves Xiaohongshu note content and engagement data from a supplied note link using Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to retrieve a Xiaohongshu note's title, body, images, and engagement counts for review or content analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit can execute remote Node tooling on the host.

Mitigation: Review the package before installation and prefer an already-provisioned qhkit installation.

Risk: Saving a Qinghu API token locally can expose provider credentials.

Mitigation: Prefer an ephemeral QHKIT_TOKEN environment variable over storing the token locally when possible.

Risk: Paid lookups consume Qinghu credits, with actual charges dependent on returned results.

Mitigation: Estimate charges and obtain user consent before paid calls; report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-rednote-note-data)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary with an optional tabular export for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include note content, image links, engagement figures, and the credits charged for paid calls.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
