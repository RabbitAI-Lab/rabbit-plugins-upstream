## Description:

Recognizes online ride-hailing itinerary receipts from local image, PDF, or archive files and returns structured OCR results through SCNet's OCR API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to extract structured trip, fare, passenger phone, and route fields from online ride-hailing itinerary receipts for downstream review or record keeping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ride-hailing itinerary files may contain passenger phone numbers, pickup and drop-off locations, trip times, fare details, and other personal or business-sensitive data.

Mitigation: Only submit files that the user is authorized to process, and make clear that selected files are sent to SCNet's OCR service.

Risk: The SCNet API key can be exposed if pasted into chat or stored with broad file permissions.

Mitigation: Store SCNET_API_KEY in environment configuration or config/.env, keep config/.env restricted to the owner, and avoid sharing the key in conversation logs.

Risk: Changing SCNET_API_BASE can redirect receipt uploads and credentials to an unintended service.

Mitigation: Keep the documented HTTPS API base unless the operator intentionally trusts and controls the alternate endpoint.

Risk: High-volume or parallel calls can hit SCNet OCR rate limits.

Mitigation: Run OCR calls serially when possible and rely on the skill's retry behavior for 429 responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/online-car-hailing-itinerary-ocr)
- [Server-resolved GitHub source](https://github.com/SCNet-sugon/online_car_hailing_itinerary_ocr)
- [SCNet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md)
- [Ride-hailing itinerary field summary](assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Pretty-printed JSON on standard output, with user-facing error text on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and accepts an optional SCNET_API_BASE override; removes confidence fields from returned OCR items before printing.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact SKILL.md, skill.yaml, and CHANGELOG.md declare 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
