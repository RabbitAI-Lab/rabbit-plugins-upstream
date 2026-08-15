## Description:

Guides agents through requirements, technical design, task planning, and confirmation checkpoints before medium-to-large implementation work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to turn larger or unclear software requests into explicit requirements, technical designs, and implementation task plans before coding begins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow intentionally slows larger work by adding requirements, design, task planning, and confirmation checkpoints.

Mitigation: Use the documented decision rule to skip the full workflow for small, precise, low-risk tasks.

Risk: The skill can direct an agent to write planning files in the project workspace.

Mitigation: Review the generated requirements, design, and task plan before allowing implementation to begin.

Risk: Specialized UI or data-model guidance may depend on sibling local skills that are not present in every installation.

Mitigation: Install the full plugin when sibling skill guidance is required; do not fetch remote skill text into context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide)
- [Publisher profile](https://clawhub.ai/user/binggg)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown planning documents and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create requirements, design, and task planning files under specs/<spec_name>/ after user confirmation.]

## Skill Version(s):

1.18.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
