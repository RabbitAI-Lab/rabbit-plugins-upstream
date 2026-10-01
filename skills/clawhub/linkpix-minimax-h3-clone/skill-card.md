## Description:

Helps agents use LinkPix and qhkit to analyze a source short-form video, rewrite its selling script for a user's product, and generate a MiniMax H3 commerce video with similar structure, voice, and emotion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External content, ecommerce, and livestream teams use this skill to turn a reference short-form video link into an adapted sales script and generated commerce video through qhkit. Agents also use it to check available MiniMax H3 model labels, estimate credits, poll task status, and deliver completed video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run Node/npm tooling and the qhkit package, including unpinned or latest package installs.

Mitigation: Install trusted, pinned versions of Node and qhkit where possible, verify downloaded binaries before use, and review package updates before running generation commands.

Risk: The skill may upload referenced local or remote media to the qhkit service for analysis or video generation.

Mitigation: Use only media the user is authorized to process, avoid sensitive source material, and confirm the exact assets before submitting generation jobs.

Risk: The skill handles a qhkit API token and may store it locally through qhkit configuration.

Mitigation: Prefer environment-variable secret injection such as QHKIT_TOKEN, avoid pasting API keys into chat when possible, and rotate tokens if exposure is suspected.

Risk: Generation commands can consume credits and create tasks that cannot be canceled after submission.

Mitigation: Run estimates when supported and require explicit user confirmation of model, duration, assets, language, and expected credits before calling generate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-minimax-h3-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten scripts, model-selection guidance, credit estimates, task IDs, polling status, and generated video URLs.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
