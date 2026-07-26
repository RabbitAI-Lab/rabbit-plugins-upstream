## Description: <br>
Create and deploy single-page static websites to GitHub Pages with autonomous workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomeksolutions](https://clawhub.ai/user/thomeksolutions) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to generate static website files, initialize a GitHub Pages project, and deploy portfolio, CV, landing page, or similar single-page sites. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated websites may expose secrets, personal data, or proprietary material if reviewed content is published as-is. <br>
Mitigation: Review all generated site files before deployment and remove confidential or inappropriate content. <br>
Risk: Deployment can create a public GitHub repository, push files, and make a GitHub Pages site live. <br>
Mitigation: Confirm repository visibility and target project details before deployment, and use GitHub credentials with only the permissions needed for the target repository. <br>


## Reference(s): <br>
- [Workflow Documentation](artifact/references/workflow.md) <br>
- [Design Patterns and Best Practices](artifact/references/design-patterns.md) <br>
- [GitHub CLI](https://cli.github.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and generated HTML, CSS, JavaScript, README, and GitHub Actions workflow files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a public GitHub repository and publish a GitHub Pages site when the deployment script is run with authenticated GitHub CLI access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
