## Description: <br>
Writes platform-native social media captions in the brand's voice for Instagram, LinkedIn, TikTok, Facebook, X/Twitter, Threads, Pinterest, YouTube, and Bluesky. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketing teams, and content creators use this skill to draft brand-voice social media captions tailored to a platform, asset, goal, topic, and call to action. It is intended for caption copy and short social post text, not scheduling, posting, long-form LinkedIn posts, threads, or video scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local brand-profile.md and voice.md files to match brand voice. <br>
Mitigation: Review those files before use and avoid placing secrets or unrelated sensitive content in them. <br>
Risk: Platform caption limits, link behavior, and hashtag norms can change. <br>
Mitigation: Re-check current platform requirements before relying on exact limits or platform-mechanics guidance. <br>
Risk: Broad caption requests may activate this skill when a specialized long-form post, thread, or video-script skill is more appropriate. <br>
Mitigation: Confirm the requested channel and format, then hand off to the specialized related skill when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/caption-writer) <br>
- [Platform mechanics](references/platforms.md) <br>
- [Caption frameworks](references/frameworks.md) <br>
- [Caption formats](references/formats.md) <br>
- [First-line guidance](references/first-line.md) <br>
- [Caption examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Usually returns 2-3 distinct caption options and one recommended option; may ask one or two clarification questions when platform or goal is missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
