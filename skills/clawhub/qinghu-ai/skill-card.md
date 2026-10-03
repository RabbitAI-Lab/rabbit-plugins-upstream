## Description:

青虎AI helps agents use Qinghu media workflows for ecommerce images, videos, translations, edits, storyboards, ad materials, POD graphics, and workflow or data-analysis tasks through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce content operators use this skill to route media-production requests to qhkit commands for product imagery, marketing videos, translation, editing, storyboard creation, ad materials, POD assets, and Qinghu workflow tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or update npm/Node tooling on the host.

Mitigation: Review the package source and run the skill in a sandboxed environment where host-level tooling changes are acceptable.

Risk: The skill can upload local media files to qhkit workflows.

Mitigation: Use only media approved for Qinghu processing and avoid passing sensitive or private files unless the deployment has approved that data flow.

Risk: The skill collects and persists a qhkit API key for ongoing use.

Mitigation: Prefer platform secret storage or environment variables, avoid sending API keys through chat, and rotate keys if they are exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ai)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters; qhkit command results are one-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return media URLs, generated scripts, prompts, task IDs, status results, and credit estimates from qhkit.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
