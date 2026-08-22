## Description:

Entry point for PPT generation that asks the user to choose fast, standard, or creative mode, collects presentation parameters, parses uploaded pdf/docx/md/txt files, writes task_pack.json and info_pack.json, and dispatches to sn-ppt-creative or sn-ppt-standard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start a new presentation workflow, choose the generation mode, supply role, audience, scene, page count, language, source document, image, chart, and output preferences, and hand off a prepared deck workspace to downstream PPT generation skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded PDF, DOCX, Markdown, and text files are parsed and may contain untrusted content or embedded images.

Mitigation: Use trusted documents where possible, keep parser dependencies pinned and patched, and review extracted raw_documents.json content before relying on it for important presentations.

Risk: The skill calls downstream model helpers for document digestion and image captioning, which can expose uploaded content to configured model services.

Mitigation: Confirm the configured model endpoints and API keys are appropriate for the document sensitivity before processing private or regulated material.

Risk: Generated deck artifacts and extracted images are written under the workspace and a local progress workbench may be started.

Mitigation: Run the skill in a workspace with appropriate file permissions, keep generated deck directories out of public sync locations, and expose the progress workbench only on trusted hosts.

Risk: Standard mode web image search requires a Serper API key and can introduce externally sourced images.

Mitigation: Use web search only when external image sourcing is acceptable, verify image suitability and rights before publication, or choose AI-generated or no-image modes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-ppt-entry)
- [Publisher profile](https://clawhub.ai/user/sensenova-skills)
- [PPT common conventions](artifact/references/conventions.md)
- [ask_user templates](artifact/references/ask_user_templates.md)
- [Serper API](https://serper.dev)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task_pack.json, info_pack.json, optional raw_documents.json, extracted document image files, image captions, and local progress workbench launch output before handing off to downstream presentation generation skills.]

## Skill Version(s):

2026.8.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
