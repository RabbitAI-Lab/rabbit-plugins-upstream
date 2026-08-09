## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and site operators use AEO to audit public, staging, local, or static websites for answer-engine optimization, schema quality, AI access files, platform detection, and deployment regressions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch public websites or explicitly approved local and private targets during audits.

Mitigation: Use local/private auditing only with explicit opt-in and keep the permission scoped to the intended target host.

Risk: Generated files or proposed fixes can affect crawler access, AI-content permissions, and structured data on a site.

Mitigation: Review proposed edits before approval, especially robots.txt, llms.txt, llms-full.txt, and AI-access signals.

Risk: The skill runs a published CLI with user-supplied URLs, paths, and flags.

Mitigation: Validate targets, quote each argument, pass flags as literal tokens, and reject shell metacharacters before running commands.

## Reference(s):

- [AEO homepage](https://ainyc.ai)
- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON or agent-format audit reports, shell commands, code changes, and limited AEO-related files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write llms.txt, llms-full.txt, and robots.txt during file-generation or fix workflows; local or private audits require explicit opt-in.]

## Skill Version(s):

4.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
