## Description:

Turns articles and documents into narrated explainer videos using dLazy's hosted video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and other users can turn articles or documents into narrated explainer, training, or report videos through a project-based dLazy workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article text and attached documents are sent to dLazy's hosted service; attachments are uploaded to dLazy storage.

Mitigation: Avoid attaching sensitive documents unless you trust the service and are authorized to share them.

Risk: The dLazy CLI may save an API key on the local machine.

Mitigation: Protect the local key and rotate or revoke it through dLazy if it is exposed.

Risk: A global CLI installation persists on the machine.

Mitigation: Use the documented pinned npx invocation if you do not want a global install.

## Reference(s):

- [dLazy CLI source (external dependency)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation runs through the dLazy hosted service; responses can be continued by project.]

## Skill Version(s):

1.0.35 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
