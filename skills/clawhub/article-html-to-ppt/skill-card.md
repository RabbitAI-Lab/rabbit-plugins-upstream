## Description:

Author professional, editable PPTX decks from Markdown, HTML, text, PDF, data, or a user template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillmelody](https://clawhub.ai/user/skillmelody)

### License/Terms of Use:

Apache-2.0

## Use Case:

External users, developers, and presentation authors use this skill to convert source material into editable PPTX decks with source-backed narrative planning, template-aware composition, speaker notes, and verification gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may execute user- or model-provided Python during deck-generation workflows with broad local privileges.

Mitigation: Run it in a sandbox or disposable project environment, review third-party author_script or refine scripts before execution, and avoid exposing secrets in the environment.

Risk: Cloud export can transmit source content, generated slide text, and relevant metadata to Feishu/Lark.

Mitigation: Prefer local PPTX output for sensitive material and use cloud export only when the user explicitly requests it and the destination is appropriate.

Risk: Final deck quality is run-specific and can depend on a capable model plus rendered visual review.

Mitigation: Treat generated decks as candidates until structural inspection, real rendering, source-bound QA, and visual approval pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillmelody/skills/article-html-to-ppt)
- [README.en.md](README.en.md)
- [PPT Smith v4.1.0 Beta 1 Release Notes](docs/v4.1.0-beta.1-release-notes.md)
- [PPT Smith v4.1.0 Beta 1 Release Readiness](docs/v4.1.0-beta.1-release-readiness.md)
- [PPT Smith V4 Bespoke Architecture Plan](docs/v4-bespoke-architecture-plan.md)
- [PPT Smith V4 Template Route](docs/v4-template-route.md)
- [PPT Smith V4 Three-Route Architecture](docs/v4-three-route-architecture.md)
- [Bundle Audit](references/BUNDLE-AUDIT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated deck, QA, and configuration artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce editable PPTX files, speaker notes, HTML previews, Feishu/Lark export instructions, manifests, and QA reports depending on the requested route.]

## Skill Version(s):

4.1.0-beta.1 (source: SKILL.md frontmatter, VERSION, README.en.md, packaging/identity.json, release notes)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
