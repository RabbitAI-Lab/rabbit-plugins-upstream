## Description:

Run AEO audits, preview branch audits, changed-page sitemap audits, local/private preview audits with explicit opt-in, sitemap origin rewriting, static-output audits, regression comparisons, site fixes, schema validation, and llms.txt generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site owners, and SEO engineers use this skill to audit and improve a website's answer-engine visibility, structured data, AI-readable files, crawler access, and regression posture across deployed, preview, local, and static-output targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a mutable npm CLI through npx.

Mitigation: Install only if the Canonry npm package and repository are trusted, and review the package source or lock execution in a controlled environment before broad use.

Risk: The skill can audit local or private preview targets when explicitly allowed.

Mitigation: Use it only on sites and local projects the operator is authorized to audit, and keep unrelated credentials out of the execution environment.

Risk: Fix and llms.txt workflows can propose or write changes to site files.

Mitigation: Review proposed edits before allowing file changes and rerun targeted audits after applying fixes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arberx/skills/aeo)
- [Canonry homepage](https://canonry.ai)
- [Repository listed by skill](https://github.com/Canonry/aeo-audit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON or agent-format audit summaries, code/configuration edits, and generated text files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update llms.txt, llms-full.txt, and robots.txt when the user requests file generation or fixes.]

## Skill Version(s):

7.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
