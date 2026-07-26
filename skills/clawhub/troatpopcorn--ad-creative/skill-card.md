## Description: <br>
Helps users generate, iterate, and scale ad creative, including headlines, descriptions, primary text, visual directions, and full ad variations for paid advertising platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[troatpopcorn](https://clawhub.ai/user/troatpopcorn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, growth operators, and agents use this skill to produce paid-ad copy and creative variations for platforms such as Google Ads, Meta, LinkedIn, TikTok, and Twitter/X. It also helps analyze supplied performance data, identify winning patterns, and propose new variations within platform limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill references campaign-management commands and may be used in an environment with ad-platform accounts, API keys, or budget authority. <br>
Mitigation: Use the skill for drafting and analysis by default; require explicit human approval before campaign creation, campaign changes, asset uploads, or any action that can spend budget. <br>
Risk: The skill includes voice-cloning and voice-generation workflows for ad audio. <br>
Mitigation: Require documented consent and rights review before cloning or generating a voice that represents a real person or brand spokesperson. <br>
Risk: Generated ad copy or visuals may conflict with brand, regulatory, or platform policy requirements. <br>
Mitigation: Review outputs against the user's stated compliance constraints and the target platform's ad preview or policy checks before launch. <br>


## Reference(s): <br>
- [Platform Specs Reference](references/platform-specs.md) <br>
- [Generative AI Tools for Ad Creative](references/generative-tools.md) <br>
- [Gemini Image Generation](https://ai.google.dev/gemini-api/docs/image-generation) <br>
- [Replicate Flux 2 Pro](https://replicate.com/black-forest-labs/flux-2-pro) <br>
- [BFL API Documentation](https://docs.bfl.ml/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with tables, lists, CSV examples, code blocks, shell commands, and structured iteration reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include platform-specific character counts, bulk-upload CSV structures, performance summaries, visual prompts, and tool-specific workflow guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter metadata reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
