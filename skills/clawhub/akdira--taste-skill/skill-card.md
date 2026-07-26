## Description: <br>
Anti-slop frontend skill for landing pages, portfolios, and redesigns that helps an agent read the brief, infer the right design direction, use real design systems when applicable, and apply strict pre-flight checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and design-focused builders use this skill to guide frontend work for landing pages, portfolios, and redesigns. It helps agents read the brief, choose an appropriate design direction, select real design systems where applicable, and apply pre-flight checks before shipping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can strongly steer frontend design choices and may suggest third-party packages, image-generation tools, or hosted visual assets. <br>
Mitigation: Review dependency, provider, and hosted-asset choices during project work, especially when strict dependency control, offline-only execution, or external-provider limits apply. <br>
Risk: The artifact is instruction-only and ships no executable code, but generated frontend output can still introduce accessibility, dependency, or visual-quality issues. <br>
Mitigation: Apply the skill's dependency checks and pre-flight review criteria, then run the project's normal tests, accessibility checks, and security review before deployment. <br>


## Reference(s): <br>
- [Taste Skill on ClawHub](https://clawhub.ai/akdira/taste-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/akdira) <br>
- [Material Web](https://m3.material.io/develop/web) <br>
- [Fluent UI React Components](https://fluent2.microsoft.design/components/web/react/) <br>
- [Fluent UI Web Components](https://learn.microsoft.com/en-us/fluent-ui/web-components/) <br>
- [Carbon Design System](https://carbondesignsystem.com/) <br>
- [Shopify Polaris](https://cdn.shopify.com/shopifycloud/polaris.js) <br>
- [Radix Themes](https://github.com/radix-ui/themes) <br>
- [shadcn/ui](https://github.com/shadcn-ui/ui) <br>
- [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) <br>
- [U.S. Web Design System](https://github.com/uswds/uswds) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a design read, design-system selection guidance, dependency checks, frontend code, asset guidance, and pre-flight review criteria.] <br>

## Skill Version(s): <br>
2.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
