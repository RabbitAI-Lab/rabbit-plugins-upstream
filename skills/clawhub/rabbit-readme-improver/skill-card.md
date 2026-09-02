## Description:

Drafts new READMEs and audits, restructures, or improves existing README.md files using measured patterns from 100 trending GitHub repositories and optional saved voice profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whit3rabbit](https://clawhub.ai/user/whit3rabbit)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and maintainers use this skill to create project READMEs, review existing README.md files, restructure sections, add focused sections such as badges or installation notes, and keep prose aligned with a chosen author voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads project documents and voice-profile files to draft or check README content.

Mitigation: Run it only on repositories and voice profiles that the agent is allowed to inspect, and keep secrets out of README inputs.

Risk: The optional --apply-model flow can send flagged passages to a user-configured model endpoint.

Mitigation: Use --apply-model only with a trusted endpoint that you configured yourself, and do not accept .rabbit-model files from untrusted repositories.

Risk: Generated README edits can introduce inaccurate commands, version claims, links, or project descriptions.

Mitigation: Review generated prose against the actual repository, run the bundled README checker, and verify install commands and license statements before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whit3rabbit/skills/rabbit-readme-improver)
- [README patterns catalog](references/patterns.md)
- [README self-check](references/checklist.md)
- [Craft guidance](references/craft.md)
- [ASD-STE100 Simplified Technical English notes](references/ste.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose, README.md content, audit findings, code blocks, and optional JSON or SARIF checker output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper scripts require python3. Remote rewrite assistance is opt-in and only used when an endpoint is explicitly configured.]

## Skill Version(s):

0.5.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
