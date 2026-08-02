## Description: <br>
The FLUX craft skill helps agents choose FLUX image-generation variants and licenses, write on-brand scene prompts and edit instructions, and keep human review, provenance, and publishing checks in the workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and marketing teams use this skill to generate and edit on-brand FLUX image prompts while selecting an appropriate model variant and license path. The skill is designed for agent-assisted prompt drafting, API-call guidance where connected, and human review before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected FLUX/BFL or third-party API credentials may authorize image-generation or editing calls. <br>
Mitigation: Scope connected credentials appropriately before installing or running the skill, as directed by the ClawHub security guidance. <br>
Risk: Commercial rights depend on the actual FLUX variant, hosting path, and current model license terms. <br>
Mitigation: Verify current BFL and model-card license terms for the selected variant before commercial use, especially for self-hosted dev-weight deployments. <br>
Risk: Generated images can create likeness, intellectual-property, provenance, disclosure, or data-honesty issues if shipped without review. <br>
Mitigation: Keep the required human review step before publication, use only permitted likenesses and original concepts, preserve provenance metadata, and apply AI disclosure where required. <br>
Risk: FLUX capabilities, pricing, and license terms can become stale as model releases change. <br>
Mitigation: Refresh claims against current provider documentation before relying on benchmarks, prices, model capabilities, or licensing details. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/social-media-skills/skills/flux) <br>
- [The PIXEL framework - FLUX images that are on-brand and on-license](references/the-pixel-framework.md) <br>
- [The reality of FLUX in 2026](references/flux-2026-reality.md) <br>
- [Prompt patterns, decision tables and worked examples](references/prompt-patterns-and-templates.md) <br>
- [Scope, distinctions and connections](references/scope-and-connections.md) <br>
- [Evaluation cases](evals/evals.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with scene prompts, edit instructions, routing notes, and license checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API-call guidance when FLUX/BFL or third-party API credentials are connected; requires human image review before publishing.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
