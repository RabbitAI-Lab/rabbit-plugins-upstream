## Description:

Helps agents produce a cost-controlled course-avatar lecturer workflow with 16 landscape base-portrait recipes and a slide-first pipeline for paid courses, training modules, and knowledge-sharing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, educators, and training teams use this skill to plan AI lecturer videos around stable avatar images, text-to-speech, selective avatar-driving segments, slide-based lesson bodies, and final video assembly. It is aimed at paid courses, corporate training, public lessons, and internal LMS content where consistent lecturer identity and controlled generation cost matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a global or npx-run dLazy CLI and stores API credentials for external service access.

Mitigation: Install the CLI only from the documented package, keep API keys in the documented config or environment variable location, and rotate keys if a workstation or generated project is shared.

Risk: Course materials, local media, and generated audio or video may be uploaded to dLazy-backed services.

Mitigation: Review source materials for confidential, student, customer, or proprietary content before upload, and use only materials the publisher is allowed to process externally.

Risk: Paid credit usage can increase quickly when avatar-driving segments are long or commands are misconfigured.

Mitigation: Use dry runs where available, keep avatar-driving limited to opening, transition, and closing segments, and verify model flags before batch generation.

Risk: Generated lecturer identities can create education-advertising or disclosure issues if presented as real credentials, endorsements, or unmarked AI content.

Mitigation: Avoid claims about guaranteed outcomes, fabricated qualifications, endorsements, or institution backing, and label AI-generated lecturer content according to the target platform's requirements.

Risk: Repeated generation can overwrite chosen lecturer images or break identity consistency across a course.

Mitigation: Back up approved base portraits and set explicit output paths before reruns or batch operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Skill source overview](artifact/SKILL.md)
- [Pipeline guide](artifact/pipeline.md)
- [Recipe library](artifact/recipes.md)
- [Troubleshooting and compliance guide](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI commands, JSON payload examples, checklists, and workflow tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference local media paths, dLazy CLI flags, credit estimates, and platform compliance checks.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
