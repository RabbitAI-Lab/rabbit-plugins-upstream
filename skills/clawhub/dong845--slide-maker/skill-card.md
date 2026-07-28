## Description: <br>
Builds, redesigns, and critiques presentation-grade .pptx slide decks from user requirements, source materials, templates, or web research, with interviews, checkpoints, rendering, linting, and critic review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dong845](https://clawhub.ai/user/dong845) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, researchers, educators, and business users use this skill to plan, build, redesign, review, and hand off editable slide decks for meetings, talks, teaching, defenses, webinars, and stakeholder readouts. It is useful when a deck must be grounded in user-provided sources, existing templates, web research, or visual assets while preserving fidelity and presentation quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local deck and source materials and write generated deck assets, previews, and persistent preference files. <br>
Mitigation: Install and run it only in workspaces where that access is acceptable, and inspect or delete taste.md if cross-deck preferences should not be retained. <br>
Risk: The skill may search the web, fetch visual assets, and use generated imagery, which can introduce licensing, factual, or representational issues. <br>
Mitigation: Review sourced asset licenses and credits, verify real-subject imagery before sharing, and keep generated images as declared visual support rather than evidence-bearing content. <br>
Risk: The skill can run local Python, browser, and rendering tools and may invoke nested Codex or optional OpenAI image generation paths. <br>
Mitigation: Review commands and generated scripts before execution, avoid untrusted style or section Python files, and require explicit user approval before using paid API-backed image generation. <br>
Risk: Browser previews and raw motif HTML can carry review risk before public distribution. <br>
Mitigation: Open and inspect generated HTML previews locally before sharing them outside the workspace. <br>


## Reference(s): <br>
- [Slide Maker ClawHub page](https://clawhub.ai/dong845/skills/slide-maker) <br>
- [Project details link from server skill summary](https://github.com/addsumtech/slides_maker) <br>
- [Design principles](references/design-principles.md) <br>
- [Review rubrics](references/review-rubrics.md) <br>
- [Hand-off and iteration](references/handoff-and-iteration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Conversational guidance, checkpoint tables, JSON review results, Python build scripts, shell commands, editable .pptx files, rendered PNG previews, and optional PDF or HTML previews.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include a deck folder under the user's chosen location, generated or fetched assets, render previews, lint and critic findings, and a compact user taste profile when explicitly warranted.] <br>

## Skill Version(s): <br>
4.1.0 (source: server release evidence, created 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
