## Description:

Connects an agent to Sogni AI for image, video, music, speech, and other creative media workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to direct an agent to generate and edit media, manage creative assets, and run Sogni-hosted workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses a Sogni API key and selected local media, and hosted workflows may upload media.

Mitigation: Install only if those permissions and uploads are acceptable; provide only media intended for processing.

Risk: Remote generation workflows can incur charges.

Mitigation: Require explicit approval for paid workflows and any use of --no-confirm-cost.

Risk: The skill keeps persistent Sogni state and offers optional integrations and self-updates.

Mitigation: Review state under ~/.config/sogni and approve MCP/Codex registration or self-update actions only when wanted.

## Reference(s):

- [Sogni Creative Agent Skill release](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Sogni pricing](https://docs.sogni.ai/pricing/#spark-packs)
- [Model and sizing guide](references/models.md)
- [Hosted workflows guide](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and optional JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated media files to a user-selected local path.]

## Skill Version(s):

3.56.0 (source: release metadata, skill metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
