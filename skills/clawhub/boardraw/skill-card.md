## Description:

Boardraw turns natural-language diagram requests into editable Excalidraw whiteboard files for flowcharts, mind maps, architecture diagrams, org charts, wireframes, sticky-note boards, and sequence diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darrenli6](https://clawhub.ai/user/darrenli6)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and other users use this skill to convert workflow, architecture, planning, and brainstorming requests into editable .excalidraw whiteboard files. The normal workflow can also upload generated boards to boardraw.com for online viewing and editing after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The normal workflow uploads generated diagram content to boardraw.com using a configured API key.

Mitigation: Review diagram content before upload and avoid sensitive architecture, business, or personal diagrams unless the user is comfortable sending that content to Boardraw.

Risk: The upload helper may read BOARDRAW_API_KEY from the environment or from parent-directory .env files.

Mitigation: Use a scoped project environment for the API key and check the working directory before running uploads so unintended parent .env files are not used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/darrenli6/skills/boardraw)
- [Server-resolved GitHub provenance](https://github.com/darrenli6/boardraw.com-skill/tree/master/boardraw)
- [Excalidraw schema reference](references/excalidraw-schema.md)
- [Excalidraw](https://excalidraw.com)
- [Boardraw upload API](https://www.boardraw.com/api/keys/auth)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated Python helper code, shell commands, editable .excalidraw files, and optional Boardraw workspace links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads require BOARDRAW_API_KEY; generated .excalidraw files remain editable in Excalidraw-compatible tools.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
