## Description:

Pm Proto Prd Pin adds an interactive PRD pinning, Markdown editing, multi-version specification, and export workflow to HTML prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, UX teams, and engineers use this skill to add requirement pins to static HTML prototypes, author PRD details, manage isolated versions, and export specification deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local persistence server and installer can mutate files in a prototype workspace.

Mitigation: Install and test only in a disposable or version-controlled workspace, and keep backups before applying the injection workflow.

Risk: The bundled local server may be unsafe if exposed beyond local development use.

Mitigation: Review and harden the server before running it by binding to localhost, restricting CORS, validating filenames to safe basenames, and avoiding network exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML and JavaScript snippets, shell commands, and generated PRD data files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local prototype assets, PRD annotation data, Markdown exports, JavaScript data exports, and print-ready PDF output.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
