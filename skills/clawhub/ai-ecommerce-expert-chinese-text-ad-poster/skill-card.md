## Description:

AI电商专家｜中文文字广告图 helps ecommerce design, brand marketing, ad operations, agency, and content teams prepare IMIVA MCP workflows for Chinese text ad posters, including product-material review, budget confirmation, task submission, task lookup, and result checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and content-production teams use this skill to turn product assets, Chinese headlines, selling points, channel requirements, and budget constraints into executable IMIVA ad-poster generation and review workflows. It is intended for Chinese ecommerce poster, marketing image, KV, listing, and social-commerce content production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs a mutable external npm package for IMIVA MCP access.

Mitigation: Use a pinned or pre-reviewed package version where possible and review the skill before installing it in sensitive environments.

Risk: The MCP helper receives environment variables and a token when launched.

Mitigation: Use a dedicated low-privilege IMIVA token and avoid running the helper from shells that contain unrelated secrets.

Risk: Local product files or HTTPS assets may be sent through the IMIVA workflow.

Mitigation: Provide only assets intended for the IMIVA task and confirm file paths, permissions, and content before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-chinese-text-ad-poster)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON MCP arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit IMIVA MCP tasks, query task status, and reference local files or HTTPS product assets when configured with a valid token.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
