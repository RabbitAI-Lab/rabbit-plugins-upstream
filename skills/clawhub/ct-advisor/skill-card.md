## Description:

A conversational clinical-trial advisor that helps with methodology, regulatory evidence, operational details, quality control, sample-size handoff, and routing to sibling data skills for registry, safety, literature, and competitive-intelligence work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT-0

## Use Case:

Clinical-trial practitioners, clinicians, and students use this skill to ask clinical-development questions in plain language, receive methodology and regulatory guidance, and route data or computation requests to specialized sibling skills when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Middle and complex questions may send prompts and draft answers to the author's Coze endpoint, which is already allowlisted.

Mitigation: Do not enter confidential, patient, sponsor, credential, unpublished protocol, or internal-path information; remove the endpoint from auto_approve_endpoints or use local-only behavior for regulated work.

Risk: Privacy and credential messaging is inconsistent across the release evidence.

Mitigation: Review endpoint, credential, memory, and logging settings before deployment, and disable or adjust behavior that does not match the intended data-handling policy.

Risk: Clinical-trial and regulatory guidance may be incomplete or unsuitable for submission without expert review.

Mitigation: Validate outputs against official sources and qualified clinical, statistical, regulatory, or legal review before operational or submission use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project homepage](https://github.com/medstatstar/ct-advisor)
- [Workflow steps](references/steps.md)
- [Search sites reference](references/search-sites.md)
- [Units reference](references/units.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown conversational guidance with occasional inline commands or routing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source labels, verification notes, language-switch instructions, or handoff guidance to sibling clinical-trial skills.]

## Skill Version(s):

0.9.54 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
