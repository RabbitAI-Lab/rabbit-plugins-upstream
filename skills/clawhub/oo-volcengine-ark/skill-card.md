## Description:

Volcengine Ark routes agent requests for reading, creating, updating, and deleting Volcengine Ark data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Volcengine Ark account from an agent, including Seedance video generation task submission, listing, retrieval, cancellation, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can submit Volcengine Ark tasks and consume service resources.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: Destructive actions can cancel or delete Seedance video generation tasks.

Mitigation: Confirm the target task and get explicit approval before running destructive actions.

Risk: The skill operates against the user's OOMOL-connected Volcengine Ark account.

Mitigation: Install and use it only when the user wants agent access to that connected account.

## Reference(s):

- [Volcengine Ark homepage](https://www.volcengine.com/product/ark)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-volcengine-ark)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
