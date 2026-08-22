## Description:

深知公文写作 helps office, administrative, secretarial, and enterprise users draft, revise, review, and deliver formal Chinese workplace documents, with optional traceable search support for policy, data, standards, and case references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users in office, administrative, secretarial, and business-document roles use this skill to turn notes, meeting records, source materials, and drafts into structured formal documents such as notices, reports, requests, letters, minutes, summaries, plans, speeches, and research reports. When authoritative support is needed, it can retrieve traceable reference material and produce separate source reports alongside Word document output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The search registration flow may require a phone number and may create or recover a service account.

Mitigation: Install only if that account flow is acceptable; use non-search writing paths when policy, data, or case retrieval is not needed.

Risk: The skill can persist a plaintext DKNOWC_API_KEY entry in ~/.zshrc for later use.

Mitigation: Review the shell profile after setup, rotate or remove the key when no longer needed, and avoid sharing generated logs or profiles that may expose credentials.

Risk: Search queries and saved knowledge-base materials or writing preferences may include sensitive internal information.

Mitigation: Use the search feature only with content suitable for the provider to receive, and periodically review or remove locally saved materials and preferences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-official-doc-writer)
- [Publisher profile](https://clawhub.ai/user/dknownai)
- [Artifact README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Search policy](artifact/reference/search_policy.md)
- [Output guide](artifact/reference/output_guide.md)
- [Review checklist](artifact/reference/review_checklist.md)
- [DKnowC search service](https://open.dknowc.cn/dependable/search/)
- [DKnowC platform](https://platform.dknowc.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown prose with optional shell commands, generated DOCX files, and HTML source-reference reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create Word documents, red-head document variants, local writing preferences, search result intermediates, and traceability reports when the user authorizes or the task requires them.]

## Skill Version(s):

3.4.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
