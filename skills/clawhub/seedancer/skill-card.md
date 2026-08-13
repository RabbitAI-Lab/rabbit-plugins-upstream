## Description:

Seedancer helps agents create structured AI filmmaking prompts, asset plans, storyboard sequences, retake diagnostics, and production handoff materials for Seedance, Kling, Veo, and related image models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to turn story ideas, scripts, shot notes, or reference-media plans into structured AI video and image generation prompts. It supports single-shot prompts, multi-shot sequences, production planning, continuity handling, and failure diagnosis for AIGC filmmaking workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports prompt guidance that may encourage filter-evasion language for age, weapon, or explosive-related wording.

Mitigation: Remove or override filter-evasion guidance before production use and require transparent safety review for minors, weapons, explosives, real people, IP, and other sensitive content.

Risk: Generated prompts may involve IP, brands, real people, lyrics, or other sensitive creative content.

Mitigation: Apply the skill's safety gate before prompt generation, confirm rights and consent, and rewrite requests toward original, non-infringing descriptions when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/seedancer)
- [CINEDANCE V4 video prompt director system](references/cinedance-video-prompt.md)
- [LIRA image prompt optimization system](references/lira-image-prompt.md)
- [ACTING system](references/acting-performance.md)
- [GEO spatial layout template](references/geo-spatial-layout.md)
- [Style Prefix](references/style-prefix.md)
- [AI director methodology](references/ai-director.md)
- [Failure code diagnosis system](references/failure-codes.md)
- [Deliverable system](references/deliverable-system.md)
- [Model mechanics](references/model-mechanics.md)
- [Mode reference and interaction notes](references/modes-and-recipes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured prompt templates, production plans, shell command snippets, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should follow the user's language and may include standardized deliverable paths for assets, prompts, manifests, and sequence state.]

## Skill Version(s):

4.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
