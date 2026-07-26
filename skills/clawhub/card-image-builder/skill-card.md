## Description: <br>
Card Image Builder helps agents create card-style images, social post long images, watermarked graphics, and batch brand-aligned visual assets through local rendering commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content teams, marketers, and developers use this skill to guide local generation of branded card images, X/Twitter-style post images, watermarked assets, and batch social-media graphics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides local command execution and can write generated image files to user-selected paths. <br>
Mitigation: Run commands in a workspace you control, choose output directories deliberately, and confirm overwrite behavior before batch generation. <br>
Risk: Remote avatar or image URLs may cause outbound fetches during rendering. <br>
Mitigation: Use trusted local assets or trusted URLs only, or replace remote images with local files before rendering. <br>


## Reference(s): <br>
- [Card Image Builder on ClawHub](https://clawhub.ai/thcjp/skills/card-image-builder) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files] <br>
**Output Format:** [Markdown instructions with JSON examples and shell or Python command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead the agent to generate local image files such as PNG outputs in user-selected directories.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
