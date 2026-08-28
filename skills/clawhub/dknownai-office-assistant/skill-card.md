## Description:

深知晓办公助手 is a third-party office assistant for drafting official documents, answering policy and government-service questions with provenance, searching authoritative materials, and generating editable PowerPoint presentations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to prepare formal workplace documents, policy-grounded answers, authoritative search reports, and editable presentation files. It is suited to office workflows that need source-aware answers, local document generation, and optional PPT generation from user-provided or retrieved materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search, consulting, and outline requests may be sent to dknowc services under the user's API key.

Mitigation: Install and use the skill only when that data sharing is acceptable, and avoid submitting confidential requests unless approved for the environment.

Risk: Some PPT paths can read local files too broadly.

Mitigation: Use trusted PPTX and SVG inputs, review file paths before processing, and avoid running the PPT workflow on untrusted presentation assets.

Risk: One export path can broaden generated-file read permissions on shared Windows machines.

Mitigation: Avoid exporting confidential presentations on shared Windows hosts, or review and restrict file permissions after export.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-office-assistant)
- [Artifact README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Document Writer Task Router](artifact/doc-writer/reference/task_router.md)
- [Document Writer Output Guide](artifact/doc-writer/reference/output_guide.md)
- [Document Writer Search Policy](artifact/doc-writer/reference/search_policy.md)
- [PPT Generation Workflow](artifact/ppt-assistant/workflows/generate-pptx.md)
- [PPT Style Presets](artifact/ppt-assistant/references/style-presets.md)
- [SVG Authoring Reference](artifact/ppt-assistant/references/svg-authoring.md)
- [Third-Party Notices](artifact/ppt-assistant/THIRD_PARTY_NOTICES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text responses with optional DOCX, PPTX, HTML provenance reports, and clean Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some modes require an API key for dknowc services; document and presentation workflows write local output files.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
