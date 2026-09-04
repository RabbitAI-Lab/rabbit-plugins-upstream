## Description:

Pm Proto Prd Pin helps agents add an interactive PRD pinning, annotation, and multi-version specification layer to HTML, Vue, React, and Next.js prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[barry0-0](https://clawhub.ai/user/barry0-0)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, designers, and developers use this skill to integrate PRD annotations, rich Markdown specifications, versioned pin data, and prototype review workflows into existing front-end prototypes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default cloud sync settings, service endpoints, or credentials could expose private PRD specifications if reused without review.

Mitigation: Review and remove hardcoded Supabase and JSONBin defaults before use with private specifications; use least-privilege tokens and project-specific storage.

Risk: Browser-stored keys or GitHub tokens could be disclosed or misused during cloud or repository sync.

Mitigation: Avoid storing personal access tokens in browser storage when possible, restrict token scope, and confirm repository visibility before enabling GitHub sync.

Risk: The injector and local persistence workflow can modify project files and overwrite vendor assets.

Mitigation: Run the injector only on a backed-up project, review generated diffs before committing, and keep a recoverable copy of existing vendor assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/barry0-0/skills/pm-proto-prd-pin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to copy assets, inject scripts, and configure local or cloud persistence for prototype PRD data.]

## Skill Version(s):

1.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
