## Description:

Build and QA editable PPT decks locally; probes required tools/fonts, runs subprocess renderers in isolated work/output folders, and uses cloud export only with explicit consent.

This skill is for research and development only.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

MeowClaw Lab Non-Commercial Source License v1.0

## Use Case:

Developers, content creators, product teams, and automation builders use this skill to convert articles, Markdown, HTML, PRDs, research material, and design specifications into editable, source-aware PowerPoint decks with local QA and delivery-state reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to run freshly generated Python and local subprocess renderers.

Mitigation: Install only from a trusted publisher, run in an isolated workspace, require explicit confirmation before Path A code execution, and review generated scripts before running them.

Risk: PMO requests may be auto-routed into bundled PMO builders.

Mitigation: Confirm the intended route for sensitive work and prefer the IR/pipeline path for normal use.

Risk: Cloud export can transmit source content, generated slide text, and metadata to Feishu/Lark.

Mitigation: Use local PPTX export by default; use cloud export only after explicit user intent and a pre-upload privacy summary.

Risk: Generated decks may include a branded disclaimer slide that is not appropriate for every sensitive or client-facing delivery.

Mitigation: Review the final deck and remove or opt out of the branded disclaimer slide where the delivery context requires it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [README.en.md](README.en.md)
- [SKILL.md](SKILL.md)
- [LICENSE](LICENSE)
- [v3.0.2 license notice](docs/v3.0.2-license-notice.md)
- [Production readiness gates](references/production-readiness-gates.md)
- [Verification harness](references/verification-harness.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON contracts, command examples, generated code paths, and PPTX/QA artifact descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local PPTX decks, manifests, QA reports, repair reports, and optional cloud-export instructions when explicitly requested.]

## Skill Version(s):

3.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
