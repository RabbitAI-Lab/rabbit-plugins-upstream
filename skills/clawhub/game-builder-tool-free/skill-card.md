## Description: <br>
用自然语言生成可玩的浏览器 3D 小游戏，支持迭代修改与本地预览。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, personal creators, and game enthusiasts use this skill to turn natural-language game ideas into playable browser-based Three.js prototypes and iterate on them locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may create or modify local game files while building or iterating on a prototype. <br>
Mitigation: Run the skill in a scoped workspace and review changed files before reuse or publication. <br>
Risk: Local preview can start a localhost server for generated browser games. <br>
Mitigation: Bind preview use to local development only and stop the server when review is complete. <br>
Risk: Generated games load Three.js from jsdelivr, which requires network access on first load. <br>
Mitigation: Confirm network policy allows the CDN or replace the dependency with an approved local copy before deployment. <br>
Risk: Broad trigger wording could activate the skill outside focused game-building tasks. <br>
Mitigation: Keep use scoped to browser game generation, iteration, and preview workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/game-builder-tool-free) <br>
- [Three.js module CDN](https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js) <br>
- [Three.js addons CDN](https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks and generated browser game files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify local game files, start a localhost preview server, and load Three.js from jsdelivr.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
