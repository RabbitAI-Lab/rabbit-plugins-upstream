## Description: <br>
Automate quality gates so no change reaches production without passing tests, lint, and build. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to design, configure, and improve CI/CD pipelines that enforce linting, type checks, tests, builds, security audits, deployments, and rollback practices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CI/CD changes can affect deployments, rollbacks, auto-merge behavior, branch protection, and secret configuration. <br>
Mitigation: Review generated pipeline and deployment changes before enabling them, especially changes that can affect production release behavior. <br>
Risk: CI workflows may expose or overuse credentials if secrets are configured too broadly. <br>
Mitigation: Use separate CI credentials and avoid giving CI production secrets unless the deployment workflow truly requires them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/ci-cd-and-automation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with YAML, TypeScript, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces CI/CD recommendations and example pipeline configuration for human review before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
