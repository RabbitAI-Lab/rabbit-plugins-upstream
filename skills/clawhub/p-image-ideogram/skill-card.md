## Description:

Guides agents in generating controlled photoreal images and graphics with readable text, structured layouts, and brand colors through Pruna's P-Image-Ideogram API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, designers, and developers use this skill to guide an agent in producing photoreal images, posters, and branded graphics with controlled typography, colors, and layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation details are sent to Pruna's API.

Mitigation: Review Pruna's data-handling terms and avoid submitting sensitive material without authorization.

Risk: Generation requires a Pruna API key.

Mitigation: Keep the key in a protected environment variable and do not include it in shared outputs.

Risk: Copy-paste npx install commands may introduce supply-chain exposure.

Mitigation: Verify the PrunaAI source and use pinned or reviewed versions where reproducibility matters.

## Reference(s):

- [ClawHub p-image-ideogram release](https://clawhub.ai/pruna-ai/skills/p-image-ideogram)
- [Pruna P-Image-Ideogram documentation](https://docs.api.pruna.ai/guides/models/p-image-ideogram)
- [Ideogram 4.0 JSON prompting](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0)
- [Ideogram JSON prompting guide](artifact/references/ideogram-json-prompting.md)
- [Domain configurations](artifact/references/domain-configurations.md)

## Skill Output:

**Output Type(s):** [Images, Text guidance, Shell commands]

**Output Format:** [Image URLs or files with Markdown guidance, optional JSON prompts, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect ratio, image size, thinking level, and prompt upsampling; image generation requires a Pruna API key.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
