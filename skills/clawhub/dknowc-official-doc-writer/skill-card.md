## Description:

dknowc official doc writer helps users draft, revise, review, and package formal workplace documents, including official documents, letters, reports, meeting minutes, plans, summaries, speeches, research reports, Word documents, and optional traceable source-reference reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, office staff, secretariat teams, administrative writers, and enterprise or public-sector users use this skill to turn notes, meeting records, source materials, research inputs, or drafts into structured formal documents and Word deliverables. When policy, data, standards, or cases are needed, the skill can retrieve traceable materials through dknowc Trusted Search and produce a separate source-reference report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask the agent to collect a phone number and SMS verification code for a third-party service.

Mitigation: Use the registration flow only when search-backed work is necessary, explain why verification is needed, and continue without search when the user declines.

Risk: The skill can create or retrieve an external service credential and persist it in ~/.zshrc.

Mitigation: Confirm the user accepts persistent credential storage before registration, avoid displaying the full key, and prefer non-persistent credential handling for sensitive environments.

Risk: Sensitive government, enterprise, or internal document text may be sent to dknowc services during search-backed workflows.

Mitigation: Confirm what content will be sent before using search, avoid sending unnecessary sensitive material, and use local-only drafting when external processing is not appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-official-doc-writer)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Output guide](reference/output_guide.md)
- [Search policy](reference/search_policy.md)
- [Review checklist](reference/review_checklist.md)
- [dknowc service endpoint](https://open.dknowc.cn/)
- [dknowc management platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown drafts, .docx Word files, optional red-head Word files, and HTML source-reference reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search-backed tasks may produce a separate HTML provenance report; PDF generation is not supported.]

## Skill Version(s):

3.4.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
