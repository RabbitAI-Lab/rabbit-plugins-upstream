## Description: <br>
微信公众号排版引擎 converts Markdown articles into WeChat Official Account-compatible inline HTML and can extract visual style from WeChat article URLs, local HTML, images, PDFs, or brand documents to generate matching theme components. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content teams, and developers use this skill to format Markdown into WeChat-ready article HTML, validate platform constraints, and create reusable visual themes from existing WeChat articles or brand assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Processing remote articles and uploaded brand assets can expose the workspace to untrusted HTML, images, PDFs, or documents. <br>
Mitigation: Review the skill before installation, process sensitive assets only in trusted workspaces, and avoid shared locations for confidential brand material. <br>
Risk: The style extraction and brand workflows can write persistent theme files and update theme registration. <br>
Mitigation: Confirm output paths before running extraction workflows and inspect generated theme and index changes before keeping or distributing them. <br>
Risk: Dependency minimums for parsers and document processors may be outdated for high-risk inputs. <br>
Mitigation: Upgrade dependency minimums before processing untrusted images, PDFs, or brand manuals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/wechatlayout) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Mode A formatting workflow](artifact/references/mode-a-format.md) <br>
- [Mode B style extraction workflow](artifact/references/mode-b-extract.md) <br>
- [Mode C brand template workflow](artifact/references/mode-c-brand.md) <br>
- [Paste test checklist](artifact/references/paste-test-checklist.md) <br>
- [Requirements](artifact/requirements.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, generated HTML fragments, preview files, theme Markdown files, validation reports, and configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mode A writes article HTML, preview pages, and optional image suggestion Markdown under output/; Modes B and C write theme Markdown files and update theme registration.] <br>

## Skill Version(s): <br>
1.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
