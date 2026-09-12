## Description:

Turn a product or marketing URL, pasted script, or brief into a product launch / promo video - SaaS promos, feature reveals, product demos, app and company launches. Use when the user wants to market, launch, promote, or reveal a product; the default for any commercial URL. Site tours / showcases of a website route here too - the brief carries the show-it-as-is intent. Unclear -> /hyperframes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, product teams, and agents use this skill to turn a product URL, launch brief, pasted script, or website showcase request into a structured HyperFrames promo video project with storyboard, script, frame compositions, captions, audio metadata, and final render steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal setup can run unpinned remote CLI code and update globally installed skills.

Mitigation: Trust the HyperFrames CLI and update source before use, prefer a pinned CLI version, separately approve global skill updates, and run the workflow in an isolated workspace.

Risk: The workflow can crawl supplied URLs, write many project files, use available media credentials or API keys, and start a local preview service before rendering.

Mitigation: Review the target URL and credential availability before execution, limit secrets to the intended media providers, and inspect generated files and preview output before rendering.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/product-launch-video)
- [Story Design](references/story-design.md)
- [Visual Design](references/visual-design.md)
- [Motion Language](references/motion-language.md)
- [Cut Catalog](references/cut-catalog.md)
- [Frame Worker Delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands plus generated project files such as BRIEF.md, STORYBOARD.md, SCRIPT.md, HTML frame compositions, index.html, audio metadata, captions, snapshots, and rendered video output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates a multi-step HyperFrames workflow that captures source material, builds a design system, drafts story and script, delegates per-frame HTML composition work, assembles captions/audio, checks the result, and renders MP4 output.]

## Skill Version(s):

1.0.36 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
