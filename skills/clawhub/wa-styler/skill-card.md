## Description: <br>
Skill to ensure all messages sent to WhatsApp follow the platform's specific formatting syntax. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill when preparing outbound WhatsApp messages that need clean, mobile-friendly formatting rather than standard Markdown syntax. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WhatsApp-specific formatting can reduce fidelity if the same response is reused in Markdown-rendered channels. <br>
Mitigation: Use the skill only for WhatsApp-bound messages or reformat the response before sending it to another channel. <br>
Risk: Replacing Markdown tables and headers with simpler WhatsApp text can remove structure from dense technical content. <br>
Mitigation: Review complex or high-stakes messages after formatting to confirm the intended hierarchy and meaning remain clear. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [WhatsApp-compatible plain text using WhatsApp formatting markers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Avoids Markdown headers, tables, horizontal rules, and double-asterisk bold syntax.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
