## Description:

Extracts a unified brand visual language from product images and brand parameters, then produces structured brandGeneJson for downstream image-generation skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent workflows use this skill to define reusable brand DNA for product image sets. It analyzes uploaded product images plus brand parameters such as color, font, platform, region, and language, then prepares a complete brandGeneJson payload for downstream LinkFox image-generation orchestration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The onboarding fallback can ask the agent to install an external linkfox-onboarding package without strong source or version constraints.

Mitigation: Approve that fallback only after verifying the package source, version, and publisher; otherwise use the documented API-key and billing guidance manually.

Risk: The workflow writes LinkFox session data and assembled brandGeneJson files to local storage.

Mitigation: Run in a workspace where local session files are expected, and review generated data before sharing or reusing it downstream.

Risk: The skill depends on the LinkFox text-generation workflow for image-informed brand extraction.

Mitigation: Confirm LinkFox credentials, quota, and dependency availability before production use, and review model-derived brand choices for design accuracy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-brand-gene-extract)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON brandGeneJson payloads plus setup and execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill writes the assembled brandGeneJson to a local session data directory for downstream reuse.]

## Skill Version(s):

1.2.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
