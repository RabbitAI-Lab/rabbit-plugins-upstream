## Description:

Wraps the Ofox image API for text-to-image generation and image editing by validating parameters, making a synchronous request, saving decoded image output, and reporting usage tokens and cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this library skill as the shared execution layer for Ofox image generation and editing workflows. It is loaded directly for low-level Ofox image API calls, failed-request debugging, or plain text-to-image requests that are not handled by a scenario skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe credential loading or request-building paths could expose API keys, images, or local files.

Mitigation: Set OFOX_API_KEY through a trusted secret mechanism, never echo the raw key, and avoid sourcing dotenv files unless their full contents have been reviewed.

Risk: OFOX_API_BASE_URL can redirect requests away from the default Ofox API endpoint.

Mitigation: Leave OFOX_API_BASE_URL unset unless deliberately using a trusted test endpoint.

Risk: Real generate or edit calls are paid API spend attempts, and ambiguous network failures may not be recoverable through a job id.

Mitigation: Run the dry-run path before spending, show the resolved model and rough estimate to the user, and do not blindly retry after network failures.

Risk: --extra-form is a request-building escape hatch that can carry unexpected curl form values.

Mitigation: Use --extra-form only when every value is trusted and the caller understands curl multipart form syntax.

Risk: A completed edit request does not by itself prove the intended image change was made without unwanted redraws.

Mitigation: Compare the output against the input before delivery and confirm unchanged areas remain acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/ofox-image-core)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-image-core)
- [Ofox API key portal](https://app.ofox.ai)
- [API parameters](references/api-params.md)
- [Pricing and cost estimates](references/pricing.md)
- [Model snapshot](references/models-snapshot.json)
- [Token anchors](references/token-anchors.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command examples and script output lines; generated or edited image files are written to disk.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports model selection, status, output paths, usage token counts, and computed image cost when available.]

## Skill Version(s):

1.11.2 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
