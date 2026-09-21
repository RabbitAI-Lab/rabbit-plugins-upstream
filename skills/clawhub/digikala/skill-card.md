## Description:

Integrates with the Digikala Marketplace Open API so sellers can manage products, upload images, search categories, handle orders, and automate seller workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Digikala sellers use this skill to call the Digikala Marketplace Open API for product creation, category navigation, image uploads, order handling, and seller workflow automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect a live Digikala seller account when supplied with a seller API token.

Mitigation: Use a least-scoped token and review payloads before running save-product, assign, brand-request, save-title, or upload commands.

Risk: A token stored in ~/.digikala/token could be exposed if local file permissions or workstation security are weak.

Mitigation: Prefer short-lived environment variables when practical, restrict token-file permissions to the owner, and rotate the token if exposure is suspected.

Risk: Uploads and product or title changes modify remote marketplace data.

Mitigation: Review files and JSON payloads before execution, and test workflows against the documented sandbox before using production credentials.

## Reference(s):

- [Digikala Endpoint Reference](artifact/references/endpoints.md)
- [Digikala Open API Documentation](https://seller.digikala.com/open-api/docs)
- [Digikala Seller API Sandbox](https://github.com/salimousavi/seller_service_sandbox)
- [Server-Resolved Source Provenance](https://github.com/ehsanghaffar/skills/tree/main/skills/digikala)
- [ClawHub Skill Page](https://clawhub.ai/ehsanghaffar/skills/digikala)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-managed Digikala seller API token; selected live-account actions prompt for confirmation.]

## Skill Version(s):

0.1.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
