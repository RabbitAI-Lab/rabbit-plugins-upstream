## Description:

Helps agents turn an existing e-commerce model or mannequin photo into new model, background, or model-and-background variants while keeping the garment unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce marketers, merchandisers, and creative operators use this skill to produce localized catalog or advertising image variants from a source garment photo while preserving product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private product photos, model photos, and prompts may be sent to a selected cloud image provider.

Mitigation: Use trusted provider endpoints, run the workflow in a constrained workspace, and confirm rights and consent for all product and person imagery before generation.

Risk: Provider API keys are used by the generation workflow.

Mitigation: Use limited-scope API keys, keep credentials out of prompts and shared files, and rotate or revoke keys when access is no longer needed.

Risk: Configurable provider routing can send requests to non-default endpoints.

Mitigation: Avoid ARK_BASE_URL unless you control and verify it, and review the selected provider with dry-run or doctor checks before sending images.

Risk: Real-person or sensitive-attribute edits could be misused for unauthorized likeness changes or misleading endorsements.

Mitigation: Use the skill only with appropriate consent and rights, and do not use it to fake a specific person's endorsement or identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON-compatible CLI output when generation runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated e-commerce image files, typically JPEG, through the selected cloud image provider.]

## Skill Version(s):

1.0.9 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
