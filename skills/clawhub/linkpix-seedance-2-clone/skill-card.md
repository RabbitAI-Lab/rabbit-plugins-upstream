## Description:

Helps short-video operators use Qinghu qhkit and Seedance 2.0 to analyze a reference social video, rewrite its structure for a product, and generate a new promotional video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agent users use this skill to turn a reference short-video link and product assets into a rewritten product-video script, qhkit commands, task polling guidance, and final video delivery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill normalizes sending an API key to the agent and using it for paid external API calls.

Mitigation: Configure QHKIT_TOKEN or qhkit locally instead of pasting secrets into chat, and confirm estimates before any generate command that can spend credits.

Risk: The skill can generate videos from provided media or links, which may encourage copying protected source material too closely.

Mitigation: Use the reference only for structure and pacing, replace original素材 and wording with user-owned product assets and approved copy, and obtain explicit user confirmation before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-2-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit option, estimate, generate, and status commands plus rewritten video-script text and delivery guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
