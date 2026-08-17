## Description:

AI Delivery Spec helps agents create, review, reverse-engineer, change, baseline, and accept requirements, PRDs, prototypes, competitor material, and existing systems while keeping outputs traceable and testable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache 2.0

## Use Case:

Product, business, design, engineering, testing, compliance, and coding-agent users use this skill to manage requirement work from framing through acceptance. It produces right-sized artifacts such as requirement briefs, PRDs, prototypes, traceability records, handoff material, gate results, and acceptance evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or persist local requirement artifacts and run local validation helpers.

Mitigation: Use it from the intended project directory and review generated files or diffs before sharing, baselining, or handing work to another role.

Risk: Default zh-CN language or template behavior may be unsuitable for non-Chinese projects.

Mitigation: Set the target language or project template before distribution and check human-facing outputs for the intended audience.

Risk: Static gate results can be mistaken for browser behavior, implementation quality, business confirmation, or customer acceptance.

Mitigation: Treat gate output as structural evidence only and require the appropriate browser, business, real-system, or customer evidence before claiming those statuses.

## Reference(s):

- [README](README.md)
- [CHANGELOG](CHANGELOG.md)
- [Stages Reference](references/stages.md)
- [Lifecycle Reference](references/lifecycle.md)
- [Specify Reference](references/specify.md)
- [Prototype Reference](references/prototype.md)
- [Change and Acceptance Reference](references/change-acceptance.md)
- [Context Management Reference](references/context.md)
- [Tool Adapters Reference](references/tool-adapters.md)
- [Troubleshooting Reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON, YAML]

**Output Format:** [Markdown and structured YAML/JSON with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include requirement briefs, PRDs, prototypes, traceability records, handoff manifests, validation results, and acceptance records.]

## Skill Version(s):

5.4.6 (source: evidence.release.version and CHANGELOG, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
