## Description: <br>
Generates raster image assets for agent workflows through a local Python CLI that uses the user's ChatGPT subscription via a browser-backed or Codex-backed path. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate new bitmap assets such as photos, illustrations, icons, hero banners, mockups, sprites, and concept art into the workspace when vector or code-native graphics are not the right fit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can download and run an unpinned CLI from GitHub at runtime. <br>
Mitigation: Review or install the CLI from a trusted pinned source before enabling the skill, and avoid automatic runtime downloads in controlled environments. <br>
Risk: The skill can use the user's logged-in ChatGPT browser session or Codex session to generate images. <br>
Mitigation: Use explicit backend settings and confirm which account, browser session, and quota bucket will be used before generation. <br>
Risk: Automatic backend fallback can shift work to Codex quota when the browser-backed path is unavailable. <br>
Mitigation: Set the backend explicitly when quota control is important, and review stderr notices before retrying failed generations. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/leeguooooo/chatgpt-imagegen) <br>
- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/chatgpt-imagegen) <br>
- [chrome-use prerequisite repository](https://github.com/leeguooooo/chrome-use) <br>
- [Issue tracker](https://github.com/leeguooooo/chatgpt-imagegen/issues) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Workspace image files plus Markdown guidance and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces PNG, JPEG, or WebP assets and reports saved paths; backend choice can affect browser-session access and quota usage.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 0.16.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
