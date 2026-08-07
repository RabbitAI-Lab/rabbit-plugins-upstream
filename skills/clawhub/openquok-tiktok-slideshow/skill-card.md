## Description: <br>
Generate TikTok photo-carousel slideshows with a locked character, AI images, text overlays, and OpenQuok draft or scheduling commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ratimon](https://clawhub.ai/user/ratimon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and developers use this skill to research a channel niche, lock a reusable character, generate six TikTok slideshow images, add text overlays, and create private drafts or scheduled posts through OpenQuok. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Account warm-up and US-audience targeting guidance may encourage platform manipulation before automated posting. <br>
Mitigation: Review the warm-up and geo-targeting advice before use, and only run the workflow for accounts and content practices that comply with platform rules. <br>
Risk: Prompts, character lock images, and generated assets may be sent to remote image providers. <br>
Mitigation: Keep sensitive prompts and reference images out of remote providers, or use an approved local/provider workflow for sensitive campaigns. <br>
Risk: Image provider API keys and OpenQuok integration identifiers may be placed in local configuration files. <br>
Mitigation: Avoid storing long-lived API keys in shared config files, restrict file access to the workspace, and rotate credentials if they are exposed. <br>
Risk: The skill can create TikTok carousel drafts or scheduled posts through OpenQuok. <br>
Mitigation: Keep the default SELF_ONLY private-draft flow unless scheduled posting is intentional, and have a human review audio, caption, privacy, and timing before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ratimon/skills/openquok-tiktok-slideshow) <br>
- [OpenQuok TikTok Slideshow documentation](https://www.openquok.com/docs/other-skills/openquok-tiktok-slideshow) <br>
- [TikTok account warm-up guide](https://www.openquok.com/blog/how-to-warm-up-a-tiktok-account-to-reach-a-us-audience) <br>
- [Character lock guide](references/character-lock.md) <br>
- [Character profile template](references/character-profile.template.json) <br>
- [Channel research guide](references/competitor-research.md) <br>
- [Slide structure and hook writing guide](references/slide-structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration, Node.js shell commands, and generated image/post metadata files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides a six-slide TikTok photo-carousel workflow using OpenQuok, Node.js scripts, an image provider, and optional private-draft posting.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter and package.json report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
