## Description:

Guides agents through using LinkPix and qhkit to generate MiniMax H3 ecommerce sales videos from product images, selling points, and selected video options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, short-video teams, and advertising practitioners use this skill to generate product showcase, sales, and paid-ad short videos through qhkit-backed MiniMax H3 video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if pasted into chat.

Mitigation: Use a narrowly scoped token through a secure local secret mechanism or environment variable, and revoke any key already shared in conversation.

Risk: The workflow installs or upgrades qhkit and dependencies without pinned versions.

Mitigation: Review qhkit and its dependency chain before installation or upgrade, and install only from package sources the deployment owner trusts.

Risk: Video generation can consume credits and submitted tasks cannot be cancelled.

Mitigation: Run estimate when supported and confirm model, duration, orientation, language, inputs, and expected credits before executing generate commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes model-option lookup, parameter confirmation, task polling, and video URL delivery steps.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
