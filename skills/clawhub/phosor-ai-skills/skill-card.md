## Description:

Generate AI videos, images and speech, bring your own LoRA models, and create AI product or model photography for e-commerce through the Phosor AI platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phosor.ai](https://clawhub.ai/user/phosor.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and e-commerce teams use this skill to submit, monitor, and manage Phosor AI media generation jobs from an agent workflow. It supports text, image, audio, video, LoRA, and Image Studio operations through documented CLI and API flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media files, and LoRA files may be sent to Phosor AI.

Mitigation: Use only content intended for Phosor AI processing and review data-sharing requirements before running upload or generation commands.

Risk: Generation, Image Studio, and related commands can spend account credits.

Mitigation: Review pricing, request parameters, and cancellation behavior before submitting jobs.

Risk: Job management commands can cancel jobs, delete LoRA models, and locally record pending job IDs with short prompt snippets.

Mitigation: Confirm destructive actions before execution and avoid including sensitive text in prompts that may be stored in local pending-job records.

## Reference(s):

- [Phosor AI API Reference](references/api.md)
- [Phosor AI Homepage](https://phosor.ai)
- [Phosor AI API Documentation](https://docs.phosor.ai)
- [ClawHub Skill Page](https://clawhub.ai/phosor.ai/skills/phosor-ai-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API Calls]

**Output Format:** [Markdown guidance with shell commands, configuration notes, and JSON API/client outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PHOSOR_API_KEY and may upload selected local media or LoRA files, submit paid jobs, manage jobs, and return generated media URLs or job metadata.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, VERSION, CHANGELOG, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
