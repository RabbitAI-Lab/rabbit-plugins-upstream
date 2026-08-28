## Description:

Seedancer helps AI filmmakers turn scripts and scene ideas into structured video, image, shot, asset, and production prompts using gated directing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and production teams use this skill to convert scripts or scene requests into AI video generation prompts, pre-production assets, shot plans, bilingual JSON prompts, and quality-control guidance for Seedance, Kling, Veo, and related image models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may include confidential scripts, unreleased story bibles, client assets, or likeness references in prompts that are later sent to hosted APIs or external generation tools.

Mitigation: Confirm approval to use sensitive material before submitting it to external services, and follow the provider's data handling policies.

Risk: Generated production prompts and shot plans may be treated as final creative or compliance guidance without review.

Mitigation: Review outputs before use, especially for client work, likeness handling, safety constraints, and model-provider policy compliance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/seedancer)
- [README](README.md)
- [Release notes](release-notes.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)
- [Scene prototype routing](references/scene-prototypes.md)
- [Camera-emotion sync](references/camera-emotion-sync.md)
- [Performance micro-beats](references/performance-micro-beats.md)
- [JSON API output mode](references/json-api-mode.md)
- [Lighting rules](references/lighting-rules.md)
- [Deliverable system](references/deliverable-system.md)
- [Output format rules](references/output-format.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, structured JSON prompt objects, and concise shell or configuration snippets when a workspace setup is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit bilingual EN/ZH prompt objects and production-stage deliverables such as script analysis, creative baselines, asset prompts, shot plans, retake guidance, and diagnostic notes.]

## Skill Version(s):

7.0.0 (source: server release evidence, SKILL.md frontmatter, README, CHANGELOG, and release notes)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
