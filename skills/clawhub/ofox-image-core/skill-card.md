## Description:

Shared execution layer for the Ofox image API that helps agents validate text-to-image and image-edit requests, estimate costs before paid calls, submit synchronous requests, save generated image files, and report token usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this library skill as the Ofox image API execution layer for scenario skills, direct low-level Ofox image requests, debugging failed image requests, and plain text-to-image generation when no scenario skill is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, prompts, sensitive images, or local files can be exposed if OFOX_API_BASE_URL, dotenv loading, or advanced form fields are misused.

Mitigation: Keep OFOX_API_BASE_URL unset unless the destination has been deliberately verified, inspect dotenv files before sourcing them, avoid unsafe --extra-form values, and rotate the Ofox key if the skill was run with an unexpected API base.

Risk: Image generation and editing can incur paid API charges, including cases where estimates are rough or endpoint validation differs.

Mitigation: Use dry-run output before paid calls, show the resolved model and estimated cost to the user, and require explicit approval before submitting generation or edit requests.

Risk: Generated or edited image dimensions and edit fidelity may not match assumptions from response status alone.

Mitigation: Measure saved files when target dimensions matter and compare edited outputs against the input image before delivering them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-image-core)
- [Ofox API key settings](https://app.ofox.ai)
- [Ofox image API endpoint](https://api.ofox.ai/v1/images/generations)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-image-core)
- [api-params.md](references/api-params.md)
- [pricing.md](references/pricing.md)
- [models-snapshot.json](references/models-snapshot.json)
- [token-anchors.json](references/token-anchors.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell commands and file paths; script execution produces image files and status, token, model, and cost lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, and OFOX_API_KEY for paid API calls; dry-run cost estimation can run without the API key.]

## Skill Version(s):

1.11.2 (source: frontmatter, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
