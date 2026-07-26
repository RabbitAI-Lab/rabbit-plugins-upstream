## Description: <br>
Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search for image URLs and metadata by keyword for reference images, backgrounds, and design assets through the dLazy CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a dLazy API key and sends search terms or referenced inputs to dLazy cloud services. <br>
Mitigation: Use it only with an approved dLazy account, avoid entering secrets as search input, and rotate or revoke the API key from the dLazy dashboard when needed. <br>
Risk: Local files or piped inputs may be uploaded if passed through supported media or stdin references. <br>
Mitigation: Do not pass local files, stdin payloads, or sensitive paths unless the upload is intended and approved. <br>
Risk: The documentation does not consistently match the advertised Pixabay image-search purpose. <br>
Mitigation: Run `dlazy search_image -h` and confirm the correct options, especially the search query argument, before automating the command. <br>
Risk: The skill depends on installing or invoking a third-party CLI package. <br>
Mitigation: Prefer the pinned `npx @dlazy/cli@1.2.3` invocation for temporary use or review the package source before global installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli) <br>
- [dLazy homepage](https://dlazy.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Shell commands, Guidance] <br>
**Output Format:** [JSON response containing image result URLs and metadata, with command-line usage guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Async use can return task metadata instead of immediate outputs; saved assets and returned URLs may be hosted by dLazy services.] <br>

## Skill Version(s): <br>
1.3.6 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
