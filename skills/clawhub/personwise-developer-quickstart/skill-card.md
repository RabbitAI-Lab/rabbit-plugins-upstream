## Description:

Builds an interactive digital-human developer quickstart course from supplied API documentation, SDK guides, and reference material, with browser OAuth and approval-gated PersonWise CLI install or update when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical-adoption teams use this skill to turn supplied API or SDK materials into a first-call course that learners can interrupt with grounded voice questions. It is intended for external developer quickstarts, not internal ramp, full API reference documentation, or unsupported claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can authenticate through browser OAuth, upload user-selected materials, create courses using existing credits, and update the PersonWise CLI or skill after approval.

Mitigation: Install only when those actions are acceptable; use private access and materials_only mode for confidential or evidence-locked courses.

Risk: Installing or updating the CLI downloads and places an executable on the user's machine.

Mitigation: Require explicit approval, use only the bundled bootstrap path, verify release size and hashes, avoid sudo, and do not overwrite an unrecognized occupied target.

Risk: A generated quickstart could misstate endpoints, parameters, authentication, versions, or security guarantees if source materials are incomplete or ambiguous.

Mitigation: Treat supplied documentation as the factual authority, carry code blocks exactly, state the documentation version or date, and avoid unsupported certification, competence, or completion claims.

## Reference(s):

- [Developer Quickstart on ClawHub](https://clawhub.ai/personwiseai/skills/personwise-developer-quickstart)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON blueprints, code blocks, shell commands, and secret-free status summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the PersonWise CLI to create or update an interactive digital-human course and reports bounded, secret-free run, project, source, review, access, and URL evidence.]

## Skill Version(s):

2.1.9 (source: server release metadata and skill invocation attribution)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
