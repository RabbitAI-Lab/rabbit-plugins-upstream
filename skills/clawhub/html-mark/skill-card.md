## Description: <br>
HTML Mark helps agents add a self-contained click-to-annotate overlay to HTML pages so reviewers can drop pins, write notes, and export feedback as Markdown, plain text, JSON, or AI-ready snippets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xuxinmaxen](https://clawhub.ai/user/xuxinmaxen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and product reviewers use this skill to inject or package a browser-side annotation runtime for HTML prototypes and pages they are authorized to review, then copy structured feedback for collaboration or agent-assisted fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The annotation runtime can run in page context and store notes, selectors, and page snippets locally. <br>
Mitigation: Use it only on prototypes or pages you are authorized to review, avoid sensitive or authenticated pages, do not annotate secrets or personal data, and clear stored annotations after use. <br>
Risk: The For-AI export can package DOM content for handoff to external AI tools. <br>
Mitigation: Review and redact exported selectors, notes, and HTML snapshots before sharing them outside the reviewed environment. <br>
Risk: Hosted bookmarklets or external script URLs can introduce code from a source that changes over time. <br>
Mitigation: Prefer the local or self-contained runtime, or use a hosted script only when you control and pin the source. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xuxinmaxen/skills/html-mark) <br>
- [Live Demo](https://xuxinmaxen.github.io/html-mark/) <br>
- [Basic Usage Example](examples/basic.md) <br>
- [Advanced Bookmarklet Example](examples/advanced.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTML script snippets, shell commands, and generated bookmarklet or runtime code output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May inject or copy a self-contained browser runtime; page annotations can persist in localStorage.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
