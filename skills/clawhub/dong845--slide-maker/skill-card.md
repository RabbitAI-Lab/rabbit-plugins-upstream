## Description:

Builds, redesigns, and critiques presentation-grade editable PPTX slide decks from user prompts, source material, existing decks, or researched topics, using interviews, design planning, local rendering, linting, and critic review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to create, revise, or review editable slide decks for research, teaching, business updates, stakeholder readouts, conference talks, thesis defenses, and similar presentation workflows. It is most useful when an agent can inspect source material, plan slide structure, generate or prepare assets, build PPTX files, render previews, and run review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local rendering and utility tools over user-provided slide, SVG, image, PDF, or document inputs.

Mitigation: Run the skill in a sandbox for untrusted inputs and review generated scripts, commands, and output paths before execution.

Risk: The skill may call web or image services and use a logged-in Codex CLI for generated images.

Mitigation: Confirm that external service use is acceptable for the deck content and avoid sending confidential material to web or image-generation services.

Risk: The skill can maintain persistent preference files in the user's home directory.

Mitigation: Review or clear the preference profile when working across clients, projects, or confidentiality boundaries.

Risk: The skill can prompt for updates that modify the installed skill copy.

Mitigation: Decline update prompts unless the user intentionally wants to update the installed skill.

## Reference(s):

- [Skill Instructions](SKILL.md)
- [Design principles](references/design-principles.md)
- [Interview protocol](references/interview-protocol.md)
- [Content plan spec](references/content-plan-spec.md)
- [Deck setup](references/deck-setup.md)
- [Review rubrics](references/review-rubrics.md)
- [Codex runtime adapter](references/codex-runtime.md)
- [Image Generation for Slide Visuals](references/image-generation.md)
- [Designed plots](references/data-viz.md)
- [Non-Latin languages](references/multilingual.md)
- [Canvas formats](references/canvas-formats.md)
- [Troubleshooting and FAQ](references/troubleshooting-faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, Python build scripts, editable PPTX files, rendered slide previews, JSON review artifacts, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local rendering tools, web or image services, Codex image generation, lint checks, and critic review artifacts when available.]

## Skill Version(s):

4.9.0 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
