## Description: <br>
Beauty Diagram helps agents render Mermaid or PlantUML diagrams as polished SVG/PNG files, share links, embed URLs, and AI-generated diagram source through the bd CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levi840714](https://clawhub.ai/user/levi840714) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, documentation authors, and agents use this skill to turn Mermaid or PlantUML source into presentation-ready diagram files, shareable links, and README or documentation embeds. It can also guide paid-plan AI diagram generation when a user starts from a text description. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private architecture diagrams, internal READMEs, or sensitive Mermaid/PlantUML content may be sent to a third-party service when rendering or exporting. <br>
Mitigation: Review sensitive inputs before use and prefer local file outputs where possible. <br>
Risk: Share and embed modes can create public or third-party-hosted diagram URLs without consistently requiring explicit confirmation. <br>
Mitigation: Use share or embed modes only when the user intends hosted access, and avoid them for private diagrams. <br>
Risk: Helper scripts may run the npm CLI through npx. <br>
Mitigation: Review the CLI invocation and run it only in an environment where npm package execution is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/levi840714/skills/beauty-diagram) <br>
- [Beauty Diagram site](https://www.beauty-diagram.com) <br>
- [Beauty Diagram CLI on npm](https://www.npmjs.com/package/@beauty-diagram/cli) <br>
- [Beauty Diagram API keys](https://www.beauty-diagram.com/account/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Code, Files] <br>
**Output Format:** [Markdown guidance with bash commands, file paths, and URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce editable Mermaid or PlantUML source, SVG/PNG renders, and public share or embed URLs through the bd CLI.] <br>

## Skill Version(s): <br>
1.7.0 (source: SKILL.md frontmatter, package.json, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
