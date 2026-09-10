## Description:

Generate AI videos, images, speech, LoRA-driven media, and e-commerce product or model photography through the Phosor AI platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phosor.ai](https://clawhub.ai/user/phosor.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and e-commerce teams use this skill to have an agent submit, poll, and manage Phosor AI media-generation jobs for videos, images, speech, LoRA assets, and product or model photography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media, LoRA files, product/model attributes, and generated job metadata are sent to Phosor.

Mitigation: Use the skill only when that data sharing is acceptable for the workload; avoid submitting sensitive media or attributes without approval.

Risk: The client can read an API key fallback from the workspace and supports plain HTTP for development endpoints.

Mitigation: Prefer PHOSOR_API_KEY or --api-key, avoid storing keys in workspace files, and use --allow-http only on trusted local or development networks.

## Reference(s):

- [Phosor AI API Reference](references/api.md)
- [Phosor AI](https://phosor.ai)
- [Phosor AI API Documentation](https://docs.phosor.ai)
- [Phosor AI ClawHub Skill](https://clawhub.ai/phosor.ai/skills/phosor-ai-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, json]

**Output Format:** [JSON API responses and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI submits and polls Phosor jobs; generated media is returned as URLs or job metadata.]

## Skill Version(s):

1.1.0 (source: frontmatter, README, CHANGELOG, VERSION, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
