## Description:

Guides agents through creating ecommerce livestream avatar and AI spokesperson videos with reusable portrait recipes, scripting, TTS, avatar driving, B-roll, assembly, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and ecommerce operators use this skill to plan and run a dLazy-based workflow for product-selling avatar videos, including base portrait generation, segmented scripts, text-to-speech audio, avatar driving, B-roll, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a third-party CLI and API that may receive prompts, media inputs, and API-authenticated requests.

Mitigation: Use an isolated environment when appropriate, protect the dLazy API key and config file, and review npm package provenance before global installation.

Risk: Generated ecommerce avatar content can mislead viewers or violate platform advertising rules if claims, credentials, or AI-generated status are not reviewed.

Mitigation: Review scripts, visuals, product claims, credentials, and platform AI-content disclosure requirements before publishing.

Risk: Incorrect model parameters, prompt lengths, or media formats can cause failed requests, wasted credits, or unusable video assembly outputs.

Mitigation: Use dry runs, keep scripted segments within documented limits, pass Chinese prompts through UTF-8 JSON input files, and re-encode mixed video/audio outputs during assembly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [dLazy homepage](https://dlazy.com)
- [SKILL.md](artifact/SKILL.md)
- [Pipeline guide](artifact/pipeline.md)
- [Portrait recipes](artifact/recipes.md)
- [Troubleshooting guide](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and command patterns for third-party dLazy CLI/API workflows; it does not itself render media.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
