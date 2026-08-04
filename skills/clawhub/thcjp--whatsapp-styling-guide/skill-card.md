## Description: <br>
Provides WhatsApp text-formatting rules, unsupported Markdown alternatives, human-facing style guidance, and reusable templates for notifications, customer support, marketing, and announcements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams and developers use this skill to draft and standardize readable WhatsApp message copy. It is best suited for text-only templates and formatting guidance, not WhatsApp Business API integration or rich-media message design. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests exec and write permissions even though the evidence describes it as a static WhatsApp formatting guide. <br>
Mitigation: Limit or audit those permissions before deployment, and prefer read-only use when the agent only needs formatting guidance. <br>
Risk: The artifact includes API and callback language that does not fit the static guide behavior. <br>
Mitigation: Treat API, callback, or command-execution claims as unverified unless separately confirmed by the publisher. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/whatsapp-styling-guide) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance and WhatsApp-formatted text templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language guidance; no API key required for the static guide behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
