## Description:

深知晓办公助手 is a comprehensive office-assistant skill for official-document drafting, policy and government-service consultation, authoritative material retrieval, and native editable PPT generation with source-traceable outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to draft and revise formal office documents, ask policy or government-service questions, retrieve authoritative materials, and generate editable PowerPoint presentations. Developers and operators may also use it as an agent workflow that combines local document/PPT tooling with dknowc API-backed retrieval and consultation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, search queries, phone-based registration data, and API-authenticated requests may be sent to dknowc services.

Mitigation: Use the skill only where that data sharing is approved, and confirm organizational approval before processing confidential government, HR, legal, finance, or internal strategy material.

Risk: Generated files, saved preferences, and local material libraries may retain sensitive content on the user's machine.

Mitigation: Review local outputs and permissions, and avoid long-term saving of materials or preferences unless reuse is intended.

Risk: The security scan notes relaxed exported PPT file permissions and recommends review before sensitive use.

Mitigation: Review generated PowerPoint files and their permissions before sharing or using them in controlled environments.

Risk: Untrusted PPTX files may expose document-processing risk.

Mitigation: Process untrusted PPTX inputs in a sandboxed environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-office-assistant)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [README](artifact/README.md)
- [Third-party component notices](artifact/ppt-assistant/THIRD_PARTY_NOTICES.md)
- [PPT generation workflow](artifact/ppt-assistant/workflows/generate-pptx.md)
- [PPT SVG authoring reference](artifact/ppt-assistant/references/svg-authoring.md)
- [Document writing output guide](artifact/doc-writer/reference/output_guide.md)
- [Document writing search policy](artifact/doc-writer/reference/search_policy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or text responses, local HTML provenance reports, clean Markdown, Word documents, and editable PowerPoint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call dknowc services with DKNOWC_API_KEY for retrieval, consultation, and provenance-backed answers; some document and PPT outputs are written as local files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence, released 2026-08-28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
