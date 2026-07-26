## Description: <br>
Runs a Telegram-based AnthroVision body-scan workflow that validates inputs and consent, submits a video scan, polls status, and returns structured body measurements and waist-to-hip ratio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to process a consenting adult user's single-person body scan video for fitness tracking, body measurement, movement analysis, or body-composition change monitoring. It is not for medical diagnosis, minors, non-consenting people, or videos of anyone other than the consenting user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive body videos and measurements are handled through an external AnthroVision bridge without enough detail about storage, access, retention, or deletion. <br>
Mitigation: Deploy only after confirming where videos and measurements are sent and stored, who can access them, and how deletion works. <br>
Risk: The skill could be misused for minors, medical diagnosis, non-consenting people, or videos of someone other than the consenting user. <br>
Mitigation: Require explicit consent from the adult user being scanned and reject medical, minor, non-consensual, third-party, or multi-person scan requests. <br>
Risk: The package includes unrelated security-scanning claims that do not align with the body-scan purpose. <br>
Mitigation: Review the advertised capabilities before installation and treat unrelated security-scanning features as unsupported unless separately justified and validated. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/anthrovision-telegram-body-scan) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-like structured text with scan identifiers, status fields, grouped measurements, waist-to-hip ratio, validation prompts, and timeout messages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses deterministic response formatting and avoids forwarding arbitrary upstream strings, links, commands, or untrusted text.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
