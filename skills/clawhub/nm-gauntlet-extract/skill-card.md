## Description:

Builds the gauntlet knowledge base from AST extraction and AI enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to initialize or refresh repository knowledge for Gauntlet challenges by extracting code structure, enriching entries, linking related modules, preserving annotations, and reporting coverage gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes a repository knowledge file that can include sensitive implementation details or inaccurate AI-enriched explanations.

Mitigation: Run it only in the intended repository and review .gauntlet/knowledge.json before committing or sharing it.

Risk: The workflow invokes an extractor script through CLAUDE_PLUGIN_ROOT, so an untrusted plugin installation could affect the generated knowledge.

Mitigation: Use a trusted plugin installation and verify the referenced extractor script before running the skill.

## Reference(s):

- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet)

## Skill Output:

**Output Type(s):** [Files, JSON, Analysis, Shell commands]

**Output Format:** [Markdown instructions with inline bash command and generated JSON knowledge file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes .gauntlet/knowledge.json, may preserve entries from .gauntlet/annotations/, and reports category summaries, coverage gaps, and difficulty distribution.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
