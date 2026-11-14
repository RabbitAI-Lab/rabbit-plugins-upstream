## Description:

Find the documentation of a project's direct dependencies from package.json, pyproject.toml, requirements.txt, Cargo.toml or go.mod using public registry metadata, then build an attributed llms.ink context pack. Use when the user wants their agent to know the libraries a project uses; not for private registries or vendored code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lukax](https://clawhub.ai/user/lukax)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill with an agent to find public documentation for a project's direct dependencies and assemble an attributed context pack for project work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency names, including internal names, may be disclosed when lookups are sent to public registries; part of the helper was not fully inspected in the security scan.

Mitigation: Review the suspicious verdict and incomplete scan evidence before installing, and avoid registry lookups that would disclose sensitive dependency names; follow the skill's prompt before looking up dependencies configured for a private registry.

## Reference(s):

- [llms.ink Workflows](https://llms.ink/workflows/)
- [ClawHub skill page](https://clawhub.ai/lukax/skills/ink-deps)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Dependency source lists and attributed context packs in JSON or Markdown, with shell commands and skipped-dependency explanations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Packs contain up to five distinct documentation sources; skipped dependencies are reported with reasons.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
