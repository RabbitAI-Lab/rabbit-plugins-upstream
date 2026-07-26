## Description: <br>
Safely uses a private local personal profile to help fill registration, signup, checkout, banking, KYC, and onboarding forms while prioritizing privacy, redaction, consent, and local, iCloud, or encrypted profile sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to let an agent map online form fields to a private local profile and fill registration, checkout, banking, KYC, onboarding, and login workflows with redaction and explicit approval for sensitive values. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can handle sensitive profile, payment, banking, government ID, credential, and document data. <br>
Mitigation: Confirm where the profile is stored, keep payment, bank, and password data in a password manager when possible, use redacted summaries by default, and require explicit approval before sensitive fills, uploads, or submissions. <br>
Risk: Autofill on suspicious, unrelated, or typosquatted domains could disclose personal data. <br>
Mitigation: Verify the real domain and form purpose before filling, and stop when the site identity or requested data does not match the user's task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/profile-use) <br>
- [Server-resolved source repository](https://github.com/leeguooooo/profile-use) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and redacted field summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Raw personal values are requested only when needed for the current fill action; final responses should use redacted values by default.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
