## Description: <br>
Clip2MD helps agents save web links to clip2md as Markdown and check remaining clipping quota. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kllb520](https://clawhub.ai/user/kllb520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure a clip2md token, submit webpage URLs for Markdown clipping, and query remaining quota from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a clip2md bearer token in a local JSON file under the user's home directory. <br>
Mitigation: Treat the token like a password, avoid using the skill on shared machines, and rotate the token if the local file may have been exposed. <br>
Risk: The skill sends user-provided URLs to the fixed clip2md API endpoint for clipping. <br>
Mitigation: Use it only for links intended for clip2md processing and review sensitive or private URLs before submission. <br>


## Reference(s): <br>
- [Clip2MD on ClawHub](https://clawhub.ai/kllb520/skills/clip2md) <br>
- [clip2md API endpoint](https://clip2.md/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a locally stored clip2md token for authenticated commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
