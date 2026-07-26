## Description: <br>
Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dlazyai](https://clawhub.ai/user/dlazyai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to search for royalty-free background music with short style keywords, then return candidate audio URLs and metadata for selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags the skill for review because it uses a dLazy API key and a general-purpose dLazy CLI. <br>
Mitigation: Review the skill before installing, prefer the pinned npx @dlazy/cli@1.2.3 search_audio command, and use only the intended search_audio options. <br>
Risk: Passing local files or @path-style input can send that data to dLazy. <br>
Mitigation: Avoid local file inputs and @path references unless the user explicitly intends to share that data with dLazy. <br>
Risk: Using --save downloads a returned audio URL to the local filesystem. <br>
Mitigation: Use --save only when the user explicitly wants to download an audio result and has chosen an appropriate destination path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio) <br>
- [dLazy CLI repository](https://github.com/dlazyai/cli) <br>
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON command output with audio result metadata and URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a dLazy API key; supports query, duration, result count, async, dry-run, and save options.] <br>

## Skill Version(s): <br>
1.3.6 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
