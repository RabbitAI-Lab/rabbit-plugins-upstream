## Description: <br>
Provides agents with LinkFox-mediated Temu US Returns & Refunds API guidance and scripts for querying after-sales orders, return logistics, return addresses, return labels, signatures, uploads, and carriers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, operators, and commerce agents use this skill to work with Temu US after-sales returns and refunds through LinkFox gateway scripts and reference docs. It is suited for querying after-sales records, return logistics, return addresses, label preparation and upload, signatures, and carriers. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: Broad proxy scripts can send arbitrary Temu API types through the LinkFox gateway beyond a tightly scoped returns workflow. <br>
Mitigation: Prefer the scoped returns/refunds endpoint scripts, restrict accepted API types in operational use, and avoid using the generic proxy for unrelated APIs. <br>
Risk: Raw LinkFox and Temu tokens may be exposed through command parameters, terminals, logs, or shared workspaces. <br>
Mitigation: Use controlled environments, prefer stored token keys where appropriate, avoid printing raw tokens, and rotate credentials if exposure is suspected. <br>
Risk: Saved response JSON can contain sensitive commerce, customer, order, refund, or logistics data. <br>
Mitigation: Store outputs only in access-controlled workspaces, review or delete saved linkfox output files after use, and avoid inline full responses unless needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-us) <br>
- [API Reference](artifact/references/api.md) <br>
- [Partner US Returns & Refunds Catalog](artifact/references/partner-us-catalog.md) <br>
- [Returns & Refunds API Index](artifact/references/apis/README.md) <br>
- [Temu Access Token Authorization](artifact/references/access-token.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with Python script commands and JSON API request/response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may persist full API responses under a local linkfox directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
