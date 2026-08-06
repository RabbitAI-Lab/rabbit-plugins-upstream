## Description:

Engram helps agents build, query, and maintain persistent local knowledge graphs for code, organization, infrastructure, and concept relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[morpheis](https://clawhub.ai/user/morpheis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Engram to preserve and query relationship knowledge across sessions, including architecture maps, dependency relationships, branch overlays, and freshness checks against git.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent graph storage may retain sensitive operational facts, personal relationship data, credential locations, SSH configuration details, or private-channel information across sessions.

Mitigation: Use Engram only for intentionally scoped, non-sensitive facts unless explicit need and consent exist; set a dedicated ENGRAM_DB_PATH, review stored database contents, and delete models that are no longer needed.

Risk: Stored relationship graphs can become stale and mislead architecture, dependency, or blast-radius decisions.

Mitigation: Use the documented check, diff, stale, verify, and refresh workflows to compare graph entries with the current source before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/morpheis/skills/clawdactual-engram)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON-oriented CLI usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI can store graph data locally and can export JSON-LD, JSON, or DOT representations.]

## Skill Version(s):

0.1.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
