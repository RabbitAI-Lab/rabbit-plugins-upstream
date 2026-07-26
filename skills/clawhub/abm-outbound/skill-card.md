## Description: <br>
Multi-channel ABM automation that turns LinkedIn URLs into coordinated outbound campaigns by scraping profiles, enriching contact details, locating mailing addresses, and coordinating email, LinkedIn, and handwritten-letter outreach. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dru-ca](https://clawhub.ai/user/dru-ca) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Sales, marketing, and growth teams use this skill to turn LinkedIn prospect lists into coordinated outbound campaigns across email, LinkedIn, and handwritten mail. It is intended for lawful account-based marketing workflows where the operator has an appropriate basis to collect, enrich, store, and contact prospects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow collects and enriches personal contact data, including phone numbers and mailing addresses, for coordinated outreach. <br>
Mitigation: Run it only with a lawful basis for prospect data processing, prefer business contact data, avoid home-address or personal-phone outreach unless explicitly authorized, and confirm consent, opt-out, suppression, retention, vendor-processing, and marketing-law requirements before campaign execution. <br>
Risk: Vendor API keys are required for enrichment, scraping, and handwritten-mail services. <br>
Mitigation: Use restricted vendor API keys, store them securely, rotate them when exposed, and review recipients and payloads before uploading data to third-party services. <br>
Risk: Skip-trace and enrichment results may be inaccurate or outdated. <br>
Mitigation: Verify recipient identity and address quality before use, skip records that fail review, and start with small test batches before scaling a campaign. <br>


## Reference(s): <br>
- [ABM Outbound on ClawHub](https://clawhub.ai/dru-ca/skills/abm-outbound) <br>
- [Enrichment Reference](references/enrichment.md) <br>
- [Scribeless API Reference](references/scribeless-api.md) <br>
- [Apify](https://apify.com) <br>
- [Apollo](https://apollo.io) <br>
- [Scribeless Platform](https://platform.scribeless.co) <br>
- [Instantly](https://instantly.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, API request examples, Python pseudocode, CSV examples, and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operator-facing campaign setup guidance and example API payloads; it does not itself execute outreach.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
