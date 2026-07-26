## Description: <br>
Skill to ensure all messages sent to WhatsApp follow the platform's specific formatting syntax. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and assistants use this skill when preparing WhatsApp-bound messages so responses use WhatsApp-compatible emphasis, lists, quotes, and monospace formatting instead of raw Markdown patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suppress standard Markdown structures such as headings and tables even when they would be useful outside WhatsApp. <br>
Mitigation: Use it for WhatsApp-bound responses and disable or override it for channels that require conventional Markdown or tabular output. <br>
Risk: Formatting rules can conflict with a user request for exact Markdown syntax. <br>
Mitigation: Honor explicit user formatting requirements when they supersede WhatsApp delivery needs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rubenfb23/skills/whatsapp-styler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [WhatsApp-compatible text using platform formatting markers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Avoids Markdown headers, tables, horizontal rules, and double-asterisk bold in favor of WhatsApp-readable formatting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, created 2026-01-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
