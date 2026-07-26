## Description: <br>
Creates free digital identities, professional resumes, and CVs through Talent.de, including permanent public URLs, optional PDF export, template selection, and human-in-the-loop review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rotorstar](https://clawhub.ai/user/rotorstar) <br>

### License/Terms of Use: <br>
Free-to-use <br>


## Use Case: <br>
External users and AI agents use this skill to collect approved resume details, create an online CV or resume, guide the requestor through review and template choices, and return the published CV URL, claim link, and optional PDF output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume details are sent to Talent.de and may create a persistent online CV. <br>
Mitigation: Use only details the requestor explicitly provided or approved, keep human review enabled for normal use, and confirm before publishing. <br>
Risk: Claim tokens grant edit or ownership access to the generated CV. <br>
Mitigation: Treat claim tokens like passwords and share them only with the requestor. <br>
Risk: Access-ID credentials and callback signatures can be abused if exposed. <br>
Mitigation: Store TALENT_ACCESS_ID in an environment variable, do not hardcode it, and verify callback HMAC signatures before trusting webhook data. <br>
Risk: CV content can include sensitive personal or business information. <br>
Mitigation: Avoid government IDs, passwords, financial details, private keys, and confidential business information. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rotorstar/skills/id-cv-resume-creator) <br>
- [Talent.de](https://www.talent.de) <br>
- [Talent API](https://www.talent.de/api) <br>
- [HITL Discovery](https://www.talent.de/.well-known/hitl.json) <br>
- [HITL Review](https://www.talent.de/en/hitl/review) <br>
- [Template Previews](https://www.talent.de/de/cv-template-ideas) <br>
- [CV Data Reference](reference/cv-data.md) <br>
- [Templates](reference/templates.md) <br>
- [HITL Protocol](reference/hitl.md) <br>
- [Access System](shared/access.md) <br>
- [Error Codes](shared/errors.md) <br>
- [Privacy & Data Handling](shared/privacy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP and JSON examples, API workflow instructions, and user-facing response text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce API request bodies, polling instructions, review links, public CV URLs, claim links, and optional PDF output.] <br>

## Skill Version(s): <br>
5.2.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
