## Description:

Generates and edits ecommerce main-image candidates from approved product photos, with guidance for white-background baselines, visible-difference images, content-commerce scenes, color SKU sets, and single-variable A/B test variants while preserving product facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and marketplace teams use this skill to plan and run dLazy banana-pro commands for compliant product main images and controlled A/B image tests. It is intended for workflows that start from approved product photos and require visual accuracy, platform-rule checks, and measurable image variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload product images and prompts to dLazy cloud endpoints.

Mitigation: Use only approved product files and prompts that may be shared with dLazy, and avoid including sensitive product or customer data.

Risk: The skill depends on the dLazy npm CLI and an API key that may be stored locally or supplied through DLAZY_API_KEY.

Mitigation: Prefer npx or an isolated environment for sensitive work, keep API keys scoped to the intended organization, and rotate or revoke the key if exposure is suspected.

Risk: Image generation can alter product structure, color, logo, quantities, or unsupported product claims if prompts are underspecified.

Mitigation: Start from approved product photos, explicitly list elements that must remain unchanged, use dry-run where appropriate, and review outputs against product facts and current platform rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may invoke the dLazy hosted API, upload selected product images, and return generated image URLs.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
