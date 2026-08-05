## Description:

Searches, inspects, validates, converts, indexes, and exports VERA (.vera) document archives with citation-ready results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dkylewillis](https://clawhub.ai/user/dkylewillis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and document analysts use this skill to retrieve evidence from local VERA archives, answer document-grounded questions with citations, inspect archive metadata, validate archive integrity, convert PDFs, manage local indexes, and export embedded source files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to run local vera-cli commands over user-selected files.

Mitigation: Confirm the intended archive, directory, and command scope before execution, and inspect command exit behavior before trusting output.

Risk: Conversion, index build or update, overwrite, and export operations write or replace local files.

Mitigation: Use write-capable commands only after explicit user authorization, and do not infer permission from requests that only ask to search or explain documents.

Risk: Retrieved evidence can be incomplete, weak, conflicting, or limited to figure metadata rather than image pixels.

Mitigation: Refine searches when evidence is weak, keep conflicting sources separate, cite page and heading details, and avoid visual claims unless a vision-capable tool inspected the image.

## Reference(s):

- [VERA CLI reference for agents](artifact/references/cli-reference.md)
- [VERA retrieval workflows](artifact/references/retrieval-workflows.md)
- [Server-resolved source provenance](https://github.com/dkylewillis/vera/tree/main/skills/vera)
- [ClawHub skill page](https://clawhub.ai/dkylewillis/skills/vera)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and citation formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to prefer vera-cli JSON output, check documented exit behavior, cite source pages and headings, and state evidence gaps explicitly.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
