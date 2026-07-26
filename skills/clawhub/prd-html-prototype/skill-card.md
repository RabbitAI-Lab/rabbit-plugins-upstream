## Description: <br>
Creates product requirements documents that pair a structured written PRD with an interactive single-file HTML prototype for mini-program and back-office workflows, plus GitHub Pages deployment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yrainy9321](https://clawhub.ai/user/yrainy9321) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers and product teams use this skill to diagnose or complete PRD drafts, add interactive HTML prototypes, and prepare a static review artifact for GitHub Pages. It is especially suited to Chinese PRD workflows that need both written requirements and clickable mini-program or admin screens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing a PRD/prototype to GitHub Pages can expose draft product plans or internal requirements. <br>
Mitigation: Confirm repository visibility, GitHub Pages settings, and the intended audience before deployment. <br>
Risk: The deployment workflow can overwrite index.html and add .nojekyll in the target repository. <br>
Mitigation: Verify the target repository and current index.html before publishing, and use the current remote blob SHA when updating through the GitHub Contents API. <br>


## Reference(s): <br>
- [PRD Structure Checklist and Diagnostics](artifact/references/prd-structure.md) <br>
- [Deploy Single-File HTML to GitHub Pages](artifact/references/deploy-github-pages.md) <br>
- [PRD HTML Prototype Template](artifact/assets/prd-template.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/yrainy9321/skills/prd-html-prototype) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with a reusable single-file HTML template and inline shell/API commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update index.html and .nojekyll when the user deploys the prototype to GitHub Pages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
