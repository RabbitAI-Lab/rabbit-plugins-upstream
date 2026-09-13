## Description:

Requires OFOX_API_KEY; provides a shared Ofox image API execution layer that validates text-to-image parameters, sends one synchronous request, decodes returned base64 images to files, and reports usage tokens and computed cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and scenario-skill authors use this library skill to call the Ofox text-to-image API, quote paid generations before spending, save generated image files, and debug low-level Ofox image generation failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Custom endpoint settings can redirect API calls and affect key handling, billing approval, and safety controls.

Mitigation: Leave OFOX_API_BASE_URL unset unless intentionally controlling the endpoint, and review any dotenv file before sourcing it.

Risk: Advanced JSON overrides can change the effective image-generation request.

Mitigation: Treat --extra-json as privileged and review its contents before approval and execution.

Risk: Paid image generation can incur cost, and estimates are rough before a real response returns usage tokens.

Mitigation: Run a dry run, show the resolved model and cost estimate, and require explicit user approval before sending a generation request.

Risk: Prompts and generated content are sent to a third-party image API.

Mitigation: Use the skill only when the user trusts Ofox for the use case and avoid sensitive prompts.

Risk: Safety refusals may indicate a boundary for the requested content.

Mitigation: Treat refusals as a safety signal instead of searching for another model that will accept the same prompt.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ofoxai/skills/ofox-image-core)
- [Ofox Image Core Homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-image-core)
- [Ofox API Keys](https://app.ofox.ai)
- [Ofox Image API Parameter Reference](references/api-params.md)
- [Ofox Image API Pricing](references/pricing.md)
- [Model Snapshot](references/models-snapshot.json)
- [Token Anchors](references/token-anchors.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command invocations and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY for real generation; dry-run cost estimates are rough until response usage tokens are available.]

## Skill Version(s):

1.10.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
