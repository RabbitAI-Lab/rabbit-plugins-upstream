## Description:

Slide Maker helps agents build, redesign, and critique presentation-grade PowerPoint decks from user-provided or researched material, with interviews, design checkpoints, and critic review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external presenters, educators, researchers, and developers use this skill to turn source material, existing decks, or researched topics into clear presentation decks. It is suited for research talks, stakeholder readouts, thesis defenses, teaching decks, webinars, and deck critique or redesign workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install Python dependencies into the active interpreter.

Mitigation: Use a virtualenv or container, or set SLIDE_MAKER_NO_ENV_CHECK=1 to disable automatic dependency checks and installs.

Risk: Deck rendering, image sourcing, icon fetching, and version checks may use local tools or network access.

Mitigation: Run only the needed branches, provide source assets when possible, pre-populate caches, and set SLIDE_MAKER_NO_VERSION_CHECK=1 when automatic version checks are not desired.

Risk: Third-party style.py files are executable Python when loaded.

Mitigation: Read and trust any style.py before using it, especially when it comes from outside the current project.

Risk: The Codex image-generation path may read recent Codex session data to recover generated image bytes.

Mitigation: Avoid that path by supplying images directly or using the documented OpenAI API image path after the billing gate.

Risk: Optional taste and profile files can persist preferences across decks.

Mitigation: Delete the profile file or redirect the registry when persistent cross-deck preferences are not wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dong845/skills/slide-maker)
- [SKILL.md](artifact/SKILL.md)
- [Design principles](artifact/references/design-principles.md)
- [Interview protocol](artifact/references/interview-protocol.md)
- [Review rubrics](artifact/references/review-rubrics.md)
- [Security and capabilities](artifact/references/security-and-capabilities.md)
- [Evaluation scenarios](artifact/evals/evals.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python build scripts, shell commands, JSON records, and generated presentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create .pptx decks, rendered previews, asset records, delivery notes, and validation reports in user-selected workspace paths.]

## Skill Version(s):

5.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
