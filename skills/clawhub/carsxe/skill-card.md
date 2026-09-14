## Description:

CarsXE helps agents use CarsXE vehicle data APIs for VIN decoding, license plate lookup, market value, vehicle history, safety recalls, lien and theft checks, OBD-II decoding, vehicle images, Year/Make/Model lookups, ownership lookups, and plate or VIN OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carsxe](https://clawhub.ai/user/carsxe)

### License/Terms of Use:

MIT

## Use Case:

Developers and vehicle-data users use this skill to route natural-language automotive questions to the appropriate CarsXE API endpoint and present vehicle specifications, valuations, history, recalls, ownership data, lien and theft checks, diagnostic-code details, images, or OCR results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive owner, plate, image, and bulk VIN data.

Mitigation: Use it only for authorized vehicle lookups with a legitimate need, and minimize requested fields, especially for owner, person, address, ZIP, image, and bulk VIN workflows.

Risk: Enterprise ownership access can expose personal data and incur billing per returned record.

Mitigation: Review entitlement scope before installation, avoid ownership searches unless required, and warn before high-volume ZIP ownership searches.

Risk: API keys and personal data may appear in request URLs or logs.

Mitigation: Redact the `key` query parameter and personal data from logs, transcripts, and shared outputs.

## Reference(s):

- [CarsXE API Docs](https://api.carsxe.com/docs)
- [CarsXE ClawHub Skill Listing](https://clawhub.ai/carsxe/skills/carsxe)
- [OpenClaw Quickstart](https://api.carsxe.com/docs/integrations/openclaw-quickstart)
- [CarsXE API reference](references/api-reference.md)
- [Recalls by YMM](references/recalls-ymm.md)
- [Recalls Batch](references/recalls-batch.md)
- [YMM Options](references/ymm-options.md)
- [Ownership](references/ownership.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with endpoint guidance, configuration commands, and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide authenticated CarsXE API calls and summarize JSON or CSV API results.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
