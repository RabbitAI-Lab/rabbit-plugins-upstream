## Description:

Recognizes tables in local images, PDFs, or archives by sending selected files to the Scnet OCR API and returning structured recognition data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to extract table structure and content from supplied document images or PDFs through Scnet's OCR service. It is useful when table recognition results are needed as structured JSON for downstream review or processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, PDFs, or archives are uploaded to Scnet's external OCR API.

Mitigation: Use only documents approved for that service and endpoint; avoid confidential, regulated, or proprietary content unless organizational policy permits it.

Risk: The skill requires an SCNET_API_KEY credential for API access.

Mitigation: Store the key in an environment variable or protected local config file and avoid pasting credentials into chat, prompts, logs, or shared files.

Risk: The external OCR service may reject requests because of invalid credentials, network failures, unsupported files, or rate limits.

Mitigation: Validate file paths and supported formats before use, keep credentials current, and retry or slow request volume when 429 rate-limit responses occur.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/SCNet-sugon/table_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/table-ocr-2)
- [Scnet website](https://www.scnet.cn)
- [API documentation summary](artifact/references/api-docs.md)
- [Table recognition fields summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON data on success, with text error messages for setup, authentication, network, or rate-limit failures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns recognized table elements such as table type, bounding boxes, and HTML table content; confidence values are removed by the script before output.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and changelog list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
