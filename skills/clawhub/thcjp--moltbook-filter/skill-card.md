## Description:

社区垃圾过滤 helps agents scan and filter community feeds by identifying likely spam posts from token-minting or automated accounts, supporting custom rules and shared blocklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, community operators, and automation agents use this skill to scan community subfeeds, remove likely spam from JSON feeds, and maintain filtering rules or blocklists for recurring spam patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines broad automation triggers, credential or API use, and optional callback behavior.

Mitigation: Review before installing, use it only for the intended community feed spam-filtering workflow, and confirm exactly which API key or config file it will read.

Risk: An optional callback_url could send results to an untrusted destination.

Mitigation: Avoid callback_url unless the destination is trusted, or restrict callbacks to approved endpoints.

Risk: The artifact has loose or inconsistent data-flow documentation.

Mitigation: Verify actual data flows during review and keep execution limited to read-only feed scanning and filtering.

Risk: Pattern-based spam filtering can misclassify legitimate posts or miss new spam formats.

Mitigation: Review filtered results, test new rules before use, and update blocklists or patterns as spam behavior changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/moltbook-filter)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and JavaScript configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scan summaries, filtered feed examples, custom spam rules, and blocklist updates.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter and changelog mention 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
