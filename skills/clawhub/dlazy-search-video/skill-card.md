## Description: <br>
Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for media sourcing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to dLazy and a dLazy API key may be stored locally by the CLI. <br>
Mitigation: Use DLAZY_API_KEY for per-invocation credentials when local key storage is not desired, and rotate or revoke keys from dLazy if needed. <br>
Risk: The --save option writes returned assets to a caller-provided local path. <br>
Mitigation: Use explicit trusted output paths and review downloaded files before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video) <br>
- [dLazy homepage](https://dlazy.com) <br>
- [dLazy CLI source](https://github.com/dlazyai/cli) <br>
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Guidance] <br>
**Output Format:** [JSON result envelope with video result metadata and URLs; optional local asset file when --save is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Async mode can return a generateId and status for later polling.] <br>

## Skill Version(s): <br>
1.3.6 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
