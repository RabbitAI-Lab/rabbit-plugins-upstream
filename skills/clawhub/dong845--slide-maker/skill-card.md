## Description:

Build, redesign, and critique presentation-grade slide decks for research, business, teaching, conference, stakeholder, thesis, and webinar use cases, using source material or web research and an interview-led actor-critic workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to plan, build, redesign, render, lint, and critique presentation decks and related slide formats. It is suited to cases where fidelity to supplied source material, visual quality gates, multilingual support, and iterative review are important.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic environment changes and local renderer or browser tooling can affect the active machine.

Mitigation: Install in a virtualenv or container, review installation prompts, and set SLIDE_MAKER_NO_ENV_CHECK=1 and SLIDE_MAKER_NO_VERSION_CHECK=1 when automatic installs or version checks are not acceptable.

Risk: Generated or supplied Python style and section modules may execute code during deck assembly or inspection.

Mitigation: Review third-party style.py and section modules before loading them, and use only trusted deck assets for programmable visual identity work.

Risk: Image generation fallback can read recent Codex session rollouts to extract generated image bytes.

Mitigation: Use user-supplied images or the API image path when session transcript access is not acceptable, and prefer explicit session environment variables when the fallback is used.

Risk: Network-enabled image search, icon fetching, web research, and version checks may disclose search subjects or skill update checks to external services.

Mitigation: Provide source material directly, pre-populate or redirect caches, avoid sourced-image branches, and disable automatic version checks when network minimization is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dong845/skills/slide-maker)
- [SKILL.md](artifact/SKILL.md)
- [Design Principles](artifact/references/design-principles.md)
- [Interview Protocol](artifact/references/interview-protocol.md)
- [Review Rubrics](artifact/references/review-rubrics.md)
- [Security and Capabilities](artifact/references/security-and-capabilities.md)
- [Image Generation](artifact/references/image-generation.md)
- [Data Visualization](artifact/references/data-viz.md)
- [Evaluation Scenarios](artifact/evals/evals.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, generated Python or shell commands, configuration notes, and deck files such as .pptx plus review artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local rendering, linting, asset preparation, image sourcing or generation, and critic-review workflows depending on user inputs and host permissions.]

## Skill Version(s):

5.1.0 (source: server release evidence and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
