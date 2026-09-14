## Description:

Helps social media operators and short-video creators use Qinghu AI and qhkit to analyze viral Grok-style video structures, rewrite them for their own products, and generate LinkPix videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, social media teams, and marketing operators use this skill to turn a viral video link into an analyzed script structure, adapt that structure to their own product, and submit a qhkit video generation task after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste credentials directly into chat.

Mitigation: Use a secure secret-entry method or environment variable for QHKIT_TOKEN, and avoid storing the token in conversation history.

Risk: Mutable global installs and @latest upgrades can change behavior between runs.

Mitigation: Pin qhkit and dependency versions where possible, review package provenance before installation, and run installs in a controlled environment.

Risk: Local compression and install commands operate on user files and the execution environment.

Mitigation: Run the workflow in a sandbox and only process files from trusted sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-grok-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include original and rewritten script comparisons, model selection guidance, qhkit task IDs, status polling results, credit estimates, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
