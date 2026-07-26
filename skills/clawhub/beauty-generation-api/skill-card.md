## Description: <br>
Beauty Generation API helps agents generate portrait images for professional headshots, character design, fashion visualization, and diverse representation through the gen1.diversityfaces.org API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luruibu](https://clawhub.ai/user/luruibu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide agents through API-key setup, quota checks, prompt preparation, portrait generation, status polling, and image download for professional portraits and creative character imagery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated-image prompts and the API key are sent to gen1.diversityfaces.org. <br>
Mitigation: Avoid sensitive, proprietary, or identifying prompt content and store BEAUTY_API_KEY only in locations suitable for protecting credentials. <br>
Risk: API-key signup may require personal details. <br>
Mitigation: Review the provider's terms and privacy information before signup and provide only information the user is comfortable sharing. <br>
Risk: The skill can guide generation of human portrait imagery. <br>
Mitigation: Follow the artifact's stated content boundaries for adult, professional, non-sensitive portrait and character requests, and decline prohibited or identifying uses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/luruibu/skills/beauty-generation-api) <br>
- [Beauty Generation API homepage](https://gen1.diversityfaces.org) <br>
- [API key request](https://gen1.diversityfaces.org/api-key-request) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, image files] <br>
**Output Format:** [Markdown guidance with curl commands, JSON API examples, optional script templates, and downloaded portrait image files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a user-provided BEAUTY_API_KEY; API responses include quota/status JSON and downloadable WebP, PNG, or JPEG images.] <br>

## Skill Version(s): <br>
1.2.52 (source: evidence release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
