## Description: <br>
GPT Image 2 supports text-to-image generation and image editing with reference inputs through the dLazy CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call dLazy's hosted GPT Image 2 service for image generation, image editing, and synthesis from prompts and reference images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and local image inputs may be uploaded to dLazy's hosted service. <br>
Mitigation: Use only prompts and files that are appropriate to share with dLazy, and avoid submitting sensitive or regulated content unless approved. <br>
Risk: Authentication stores a dLazy API key in local CLI configuration unless a per-run environment variable is used. <br>
Mitigation: Use OS user permissions, rotate or revoke keys when needed, and prefer DLAZY_API_KEY for short-lived runs where persistent storage is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2) <br>
- [dLazy CLI homepage](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy service homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Image URLs, Shell commands, Guidance] <br>
**Output Format:** [JSON responses with generated image URLs and task status fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports synchronous results or asynchronous generateId polling; generated media is hosted by dLazy.] <br>

## Skill Version(s): <br>
1.3.5 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
