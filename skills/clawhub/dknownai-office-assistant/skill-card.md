## Description:

DknownAI Office Assistant helps agents draft Chinese office documents, answer and retrieve policy or government-service information with sourced reports, and generate editable PowerPoint files from user materials or prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and office-support agents use this skill to prepare official documents, consult and verify policy or government-service information, retrieve authoritative materials, and produce editable PPTX presentations with supporting provenance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured DKnowC API key could be sent outside the declared service domains if custom DKNOWC endpoint variables are set.

Mitigation: Keep the default DKnowC endpoints and set custom DKNOWC_*_ENDPOINT values only for targets you trust.

Risk: Registration and some workflows involve sensitive user-provided credentials or contact information.

Mitigation: Install only when comfortable providing a DKnowC API key and, during registration, a phone number and verification code.

Risk: Optional key persistence or local material memory can save information on the user's machine.

Mitigation: Agree to key persistence or local material memory only when those values should remain saved locally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-office-assistant)
- [DKnownAI Publisher Profile](https://clawhub.ai/user/dknownai)
- [Artifact README](artifact/README.md)
- [Third-Party Notices](artifact/ppt-assistant/THIRD_PARTY_NOTICES.md)
- [DKnowC Open Service](https://open.dknowc.cn/)
- [DKnowC Platform](https://platform.dknowc.cn/)
- [ppt-master Upstream Project](https://github.com/hugohe3/ppt-master)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown responses plus generated Word, PPTX, HTML provenance reports, clean Markdown, and local configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a DKNOWC_API_KEY for consultation, retrieval, and source-backed generation paths.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
