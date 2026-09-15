## Description:

Vibe Coding Coach helps users plan, prompt, debug, review, and ship software with AI coding tools while managing context, quality, security, cost, and common failure modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

External users, founders, product managers, designers, developers, and students use this skill to choose AI coding tools, structure prompts and workflows, debug AI-built apps, and apply production-readiness checklists before shipping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad AI-coding help requests and provide advisory guidance beyond the user's exact project context.

Mitigation: Treat its responses as coaching, ask for project-specific assumptions and verification steps, and review recommendations before applying them.

Risk: Users may be tempted to share secrets, production credentials, or real customer data while debugging with AI coding tools.

Mitigation: Keep secrets in environment variables, use redacted or synthetic data in prompts, and avoid pasting credentials or sensitive customer data into AI sessions.

Risk: AI-generated changes for authentication, payments, privacy, or other sensitive features can miss security and compliance requirements.

Mitigation: Require professional review and explicit security checks before shipping sensitive features to production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/vibe-coding-coach)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown coaching guidance with prompt templates, checklists, comparison tables, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English and Chinese guidance; no execution, credential collection, persistence, or privileged access requested.]

## Skill Version(s):

3.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
