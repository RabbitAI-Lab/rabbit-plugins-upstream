## Description:

This skill helps social media operators and short-form video creators analyze viral Grok-style video examples, rewrite the structure for a product, and generate finished videos through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External content teams, social media operators, and short-form video creators use this skill to turn a reference video link into a product-specific script and qhkit video generation workflow. It supports viral-structure adaptation, model option checks, estimate-before-submit behavior, task polling, and delivery of generated video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose source links, uploaded images, uploaded video, and generation prompts to qhkit or iqinghu services.

Mitigation: Use the skill only when the user is comfortable sending those materials to the third-party service, and avoid submitting sensitive or confidential media.

Risk: The workflow depends on API credentials and the evidence notes that the skill asks users to provide an API key in chat.

Mitigation: Configure credentials locally with QHKIT_TOKEN or another secret-safe mechanism instead of pasting API keys into chat.

Risk: Generate actions can spend paid credits and cannot be cancelled after submission.

Mitigation: Run estimates when supported, summarize the concrete generation parameters and expected credits, and obtain explicit user approval before submitting paid tasks.

Risk: The skill may install persistent tooling for the third-party qhkit service.

Mitigation: Review the qhkit package and install source before use, prefer least-privilege installation paths, and upgrade only when needed for command compatibility.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-grok-clone)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu login](https://www.iqinghu.com/workbench/login?urlCode=agentch)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON qhkit parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten scripts, qhkit option and estimate guidance, task IDs, status polling instructions, and generated video URLs.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
