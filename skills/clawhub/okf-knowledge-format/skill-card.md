## Description: <br>
Create, read, validate, and manage OKF (Open Knowledge Format) knowledge bundles for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akdira](https://clawhub.ai/user/akdira) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to read, create, validate, and maintain OKF knowledge bundles made from Markdown files with YAML frontmatter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends installing okf-toolkit directly from an unpinned GitHub URL, which can change over time. <br>
Mitigation: Install the OKF CLI only from a trusted source; prefer a pinned, integrity-verifiable release or vetted package-index install. <br>
Risk: Agents may create or edit OKF bundle content that is inaccurate or malformed. <br>
Mitigation: Review generated Markdown and YAML frontmatter, then run okf validate before relying on the bundle. <br>


## Reference(s): <br>
- [OKF Spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) <br>
- [okf-toolkit](https://github.com/akdira/okf-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with YAML frontmatter examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to validate OKF bundles after changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
