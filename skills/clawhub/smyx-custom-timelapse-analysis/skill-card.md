## Description:

Generates condensed album highlights based on specified keywords or targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People organizing home, travel, or event videos can find clips matching selected people, pets, scenes, events, or keywords and review a condensed highlight reel. They can also retrieve earlier analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private videos may still be uploaded to the remote service despite an export-only request.

Mitigation: Wait for the export-only behavior to be fixed before using private footage, and confirm the provider's media retention, deletion, account creation, and pricing terms.

Risk: Service credentials are handled unsafely.

Mitigation: Wait for credential handling fixes before configuring a service secret.

Risk: The --api-url option is ignored and cannot redirect processing as advertised.

Mitigation: Do not rely on --api-url to choose the processing destination; verify the service destination before sending media.

Risk: An output path may overwrite an existing result.

Mitigation: Use a new output filename.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-custom-timelapse-analysis)

## Skill Output:

**Output Type(s):** [JSON, Markdown, analysis reports, video highlight reels, report links]

**Output Format:** [Structured analysis reports; Markdown tables for report listings; highlight reel links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include matched segments, findings, suggestions, and links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
