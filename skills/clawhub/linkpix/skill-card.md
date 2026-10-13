## Description:

Helps create and edit ecommerce images and videos, develop ad and storyboard content, and retrieve product and market data through Qinghu's paid AI services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, ecommerce sellers, and content creators use this skill to plan and produce product imagery, promotional video, and ads, and to research marketplace products and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and ecommerce queries are sent to a paid external service.

Mitigation: Confirm service use and pricing before sending sensitive material or starting paid jobs.

Risk: Sharing an API key in ordinary chat can expose account credentials.

Mitigation: Use a secure secret, environment variable, or local configuration instead of pasting keys into chat.

Risk: The skill may request global package installation, Node or PATH changes, or execution of latest-version packages.

Mitigation: Review installation and runtime changes before authorizing an agent to run them.

Risk: Watermark removal and face replacement can affect content without appropriate rights or consent.

Mitigation: Use these features only on content you are authorized to edit and with required consent.

## Reference(s):

- [LinkPix on ClawHub](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples, task results, and links to generated media or data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation and data retrieval require an external paid service; tasks may return links to images, videos, scripts, or data.]

## Skill Version(s):

0.1.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
