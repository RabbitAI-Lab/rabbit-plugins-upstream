## Description:

Provides Chinese wyx spec guardrails for declaring CONCEPT, PIPELINE, and SYNCS module boundaries and checking drift when explicitly invoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to create and review architecture boundary specifications, detect drift between specs and code, and generate architecture maps for projects that follow the wyx CONCEPT/PIPELINE/SYNCS workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled optional hook runtime can run shell scripts automatically at session start and around file edits.

Mitigation: Enable the runtime only in projects where automatic scans and edit-time context injection are acceptable; review the hook configuration before global installation.

Risk: Architecture map output can update ARCHITECTURE.md based on existing specs.

Mitigation: Review generated architecture changes before accepting them, especially when the map is used to guide later edits.

Risk: Drift checks can append lightweight history under .claude.

Mitigation: Confirm that local project policy allows this history file before using the optional drift workflow.

## Reference(s):

- [Project audit and command planning](references/audit.md)
- [Bounded concept design](references/concept.md)
- [Drift detection procedure](references/drift-detection.md)
- [Hooks runtime wiring and troubleshooting](references/hooks-runtime.md)
- [Architecture map generation](references/map.md)
- [Data pipeline specification](references/pipeline.md)
- [Sync coordination mapping](references/sync.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional generated specification files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update CONCEPT.md, PIPELINE.md, SYNCS.md, and ARCHITECTURE.md after user approval, depending on the selected mode.]

## Skill Version(s):

0.26.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
