## Description: <br>
Consent Registry helps agents record and query pseudonymous consent, lawful-basis, suppression, restore, and erasure events through an append-only consent stream. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and marketing operations teams use this skill to keep consent, suppression, restore, and erasure facts tied to pseudonymous subject IDs before downstream email eligibility or segment decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Raw contact PII could be exposed if users provide email addresses, phone numbers, names, or other direct identifiers. <br>
Mitigation: Use pseudonymous subject IDs and opaque proof references only, as directed by the server security guidance and skill contract. <br>
Risk: Consent or suppression state could be unreliable when the expected registry runtime, schema, or host controls are unavailable. <br>
Mitigation: Verify the consent registry runtime, event schema, and host-capability controls before mutation; when unavailable, return the documented handoff instead of claiming canonical state. <br>
Risk: A restore or erasure action could be accepted without the required authority or evidence. <br>
Mitigation: Require the request-bound host capability and evidence constraints described by the artifact before restore or erasure actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/consent-registry) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured handoff details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses pseudonymous subject IDs and proof references; does not store raw contact PII.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
