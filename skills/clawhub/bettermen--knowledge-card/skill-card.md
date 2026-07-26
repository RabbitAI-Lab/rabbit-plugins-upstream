## Description: <br>
Kindle知识卡片生成器 converts supplied knowledge material into high-density Kindle-style HTML cards with adaptive process, comparison, and concept layouts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, educators, and knowledge workers use this skill to turn source notes or concepts into a browser-openable Kindle-style HTML knowledge card. It is useful for concise learning artifacts, visual summaries, and shareable single-card explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may overwrite an existing index.html in the current working directory. <br>
Mitigation: Run it in a dedicated working directory or preserve any existing index.html before invocation. <br>
Risk: Generated cards load Tailwind and Google Fonts from external CDNs. <br>
Mitigation: Avoid highly sensitive source text when external network requests are not acceptable, or adapt the generated HTML to use locally approved assets. <br>
Risk: The skill may open a browser preview of generated local HTML. <br>
Mitigation: Review the generated file and browser-preview behavior in a controlled workspace before using it with sensitive content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/knowledge-card) <br>
- [README](artifact/README.md) <br>
- [Card template](artifact/references/card-template.html) <br>
- [Layout rules](artifact/references/layout-rules.md) <br>
- [Examples](artifact/references/examples.md) <br>
- [Tailwind CSS CDN](https://cdn.tailwindcss.com) <br>
- [Google Fonts stylesheet](https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Noto+Sans+SC:wght@400;500;700;900&family=Noto+Serif+SC:wght@400;700&display=swap) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Single HTML file named index.html with embedded CSS and CDN stylesheet references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May open a browser preview after writing the local HTML file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
