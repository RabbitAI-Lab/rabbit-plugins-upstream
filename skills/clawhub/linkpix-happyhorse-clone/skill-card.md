## Description:

This skill helps short-form video creators and ecommerce teams use qhkit / 青虎 AI to analyze a viral video link, rewrite it for a product, and generate a Happy Horse 1.1-style video remake.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to turn a short-video reference link into an analyzed script, product-specific rewrite, and user-approved qhkit video generation command flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask the user to provide a qhkit API key in chat.

Mitigation: Use a dedicated low-privilege key and prefer a secure secret manager or environment variable for token handling.

Risk: The skill can install or update qhkit and related runtime tooling in the user's environment.

Mitigation: Review install commands before execution and avoid automatic global installs or unpinned npx executions unless the package source and runtime environment are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-happyhorse-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash/qhkit commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit task IDs, status summaries, and final media URLs after user-approved CLI runs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
