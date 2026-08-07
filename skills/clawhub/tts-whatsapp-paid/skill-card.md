## Description: <br>
This skill helps agents prepare Piper TTS voice-message workflows for WhatsApp group broadcasts, batch sends, scheduled sends, message templates, delivery reports, and API wrapping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operations teams, and developers use this skill to draft and configure opted-in WhatsApp voice-message outreach, including personalized batch messages, scheduled reminders, and API-based delivery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk or scheduled WhatsApp outreach can contact recipients without strong built-in consent or opt-out controls. <br>
Mitigation: Use only lawful, opted-in recipient lists and add explicit consent checks, opt-out handling, and operator approval before bulk, scheduled, or API sends. <br>
Risk: API and background sending modes can be misused if exposed without authentication, rate limits, or a stop control. <br>
Mitigation: Require API authentication, rate limits, protected scheduling controls, and a clear way to cancel or stop background sends. <br>
Risk: Contact lists and send reports may contain personal or sensitive communication data. <br>
Mitigation: Store contact and report files in protected locations, restrict access, and retain only data needed for the approved communication workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/tts-whatsapp-paid) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell, Python, YAML, CSV, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command examples, configuration snippets, contact-list templates, scheduling examples, and operational guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
