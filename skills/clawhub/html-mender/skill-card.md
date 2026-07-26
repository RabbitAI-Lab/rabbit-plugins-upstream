## Description: <br>
HTML Mender helps agents turn local or saved HTML presentation pages into browser-editable copies for visual text, image, and layout edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuhaoyupku](https://clawhub.ai/user/wuhaoyupku) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content editors use this skill when they need to make small visual changes to local or saved HTML decks without regenerating the whole page. The skill prepares an editable HTML working copy and guides users to export a clean edited HTML file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill on live or authenticated pages is outside its intended local-file scope. <br>
Mitigation: Use it only with local or saved HTML files, and ask for a saved local copy before editing online or authenticated content. <br>
Risk: The editable working copy embeds the original source HTML as the baseline for clean export. <br>
Mitigation: Treat the .editable.html file as a working copy and share the downloaded clean HTML result when possible. <br>
Risk: Refreshing or closing the editable page can lose unsaved visual edits. <br>
Mitigation: Use the Download HTML action to export the durable edited result before closing or refreshing the page. <br>


## Reference(s): <br>
- [HTML Mender on ClawHub](https://clawhub.ai/wuhaoyupku/skills/html-mender) <br>
- [HTML Mender homepage](https://github.com/wuhaoyupku/html-mender) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and generated HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an editable .html working copy and a downloaded clean HTML export; requires Node.js and a local or saved HTML input.] <br>

## Skill Version(s): <br>
0.1.17 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
