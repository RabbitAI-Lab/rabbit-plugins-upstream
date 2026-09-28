## Description:

Detects flames and smoke in images or video for fire early warning in industrial parks, forests, warehouses, and similar sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security, safety, and operations teams use this skill to analyze monitoring images, videos, or URLs for flame and smoke indicators, structured findings, warnings, report links, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the skill sends media or URLs to lifeemergence.com cloud APIs, stores local identity or token data, and may reuse a fallback identity in ways that could mix report history between users.

Mitigation: Review before installation, use only where cloud processing and local credential persistence are acceptable, and avoid shared or multi-user workspaces until identity isolation is fixed.

Risk: Fire and smoke detection output is for safety warning support and may require on-site confirmation.

Mitigation: Treat results as an aid to monitoring workflows and rely on professional emergency confirmation and response procedures when fire is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection findings, warnings, report links, and historical report tables.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
