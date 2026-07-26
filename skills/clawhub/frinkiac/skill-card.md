## Description: <br>
Search TV show screenshots and generate memes from The Simpsons, Futurama, Rick and Morty, and 30 Rock. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryantenney](https://clawhub.ai/user/ryantenney) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to configure and operate a Frinkiac/Morbotron MCP server for finding TV dialogue, browsing adjacent scene frames, retrieving screenshots and episode context, and generating captioned memes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup runs an external npm MCP package through npx, which executes local code during installation or startup. <br>
Mitigation: Confirm the npm package publisher is trusted and consider pinning or reviewing the MCP package version before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ryantenney/skills/frinkiac) <br>
- [Publisher profile](https://clawhub.ai/user/ryantenney) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, API calls] <br>
**Output Format:** [Markdown instructions with MCP configuration JSON and tool call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and npx; the configured MCP server can return search results, scene metadata, screenshot URLs or image data, nearby frame data, subtitles, and meme image outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
