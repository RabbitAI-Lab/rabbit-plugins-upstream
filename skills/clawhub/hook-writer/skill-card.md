## Description: <br>
Writes truthful, format-aware opening hooks for social content, including caption first lines, short-video openings, carousel covers, thread openers, YouTube title and thumbnail concepts, and email subject and preview text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Social media marketers, creators, and content teams use this skill to turn provided content into truthful, brand-voice hooks that fit the target format and earn the next click, swipe, read, or view. The skill is especially useful when a post has useful substance but the opening is weak, vague, or too slow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local brand and voice guidance when available, so unrelated private material in those files could be exposed to the agent context. <br>
Mitigation: Keep brand-profile.md and voice.md limited to brand-relevant guidance, voice rules, and compliance guardrails; omit unrelated private or sensitive information. <br>
Risk: Hooks can become misleading if they overpromise what the content delivers, especially in sensitive or regulated topics. <br>
Mitigation: Require each hook to be true to the underlying content, reject bait-and-switch claims, and follow any brand compliance guardrails before publication. <br>


## Reference(s): <br>
- [Hook mechanisms taxonomy](references/mechanisms.md) <br>
- [Hook craft by format](references/formats.md) <br>
- [Scoring and selection rubric](references/scoring.md) <br>
- [Worked hook examples](references/examples.md) <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/hook-writer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with hook options, a recommendation, and format-specific notes when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Typically returns 2-3 distinct hook options, a one-line recommendation, and for video hooks may include opening visual, on-screen text, and first spoken words.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release, SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
