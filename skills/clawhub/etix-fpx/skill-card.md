## Description: <br>
Query etix.com event discovery data from a shell with the fpx CLI, including event, venue, and performer search plus event and venue detail through one-shot calls routed via a browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to retrieve public Etix discovery data without running the etix-mcp server. It helps agents produce setup guidance, fpx commands, endpoint recipes, and parsing steps for read-only event, venue, performer, and geolocation queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the Transporter extension and fpx to make Etix fetches through the user's browser context. <br>
Mitigation: Keep browser site access limited to etix.com and review the global npm package before installation in sensitive environments. <br>
Risk: Etix HTML responses can be DataDome interstitials even when a fetch command exits successfully. <br>
Mitigation: Check responses for DataDome markers before parsing, and refresh an etix.com tab until the browser challenge clears. <br>
Risk: Ticket purchasing and credentialed seller APIs are financial or authenticated workflows outside the skill's intended behavior. <br>
Mitigation: Use the skill only for anonymous, read-only discovery and do not extend it to purchases, Etix login flows, or venue seller APIs. <br>


## Reference(s): <br>
- [Etix consumer endpoints for fpx](artifact/references/etix-endpoints.md) <br>
- [extract-datalayer.mjs](artifact/references/extract-datalayer.mjs) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and JavaScript parsing snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Etix discovery workflows; responses may include JSON, saved HTML, JSON-LD, microdata, or dataLayer extraction steps.] <br>

## Skill Version(s): <br>
0.4.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
