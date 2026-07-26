## Description: <br>
Turns product photos, specifications, catalogs, or ecommerce listings into conversion-focused shopping ad videos with multilingual voiceover and an optional virtual host. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, ecommerce teams, and developers use this skill to start or continue dLazy projects that generate product, shopping, TikTok Shop, and ecommerce ad videos from product files or listing links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, project context, and files passed with `--files` are sent to dLazy-hosted services. <br>
Mitigation: Avoid sending sensitive content unless approved for that service, and review dLazy terms before use. <br>
Risk: The dLazy API key may be saved in `~/.dlazy/config.json`, while the referenced CLI package may not enforce the private file permissions claimed by the skill. <br>
Mitigation: Use a dedicated, revocable API key; prefer `DLAZY_API_KEY` per invocation when persistence is not needed; and verify local config file permissions after login. <br>
Risk: Global installation adds a third-party CLI package to the local environment. <br>
Mitigation: Review the dLazy CLI before installing and consider using the pinned `npx @dlazy/cli@1.2.3` path instead of a persistent global install. <br>


## Reference(s): <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a pinned dLazy CLI invocation and may reference project IDs, prompts, API-key setup, and local files supplied by the user.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
