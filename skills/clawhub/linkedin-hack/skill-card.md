## Description:

Tinker LinkedIn lets an agent query LinkedIn profiles, search results, companies, connections, inbox threads, feed items, and message drafts through a user-shared signed-in LinkedIn browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect their own LinkedIn account context for research, triage, and relationship-management workflows while they keep a signed-in LinkedIn tab shared locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive LinkedIn account data through a signed-in shared tab, including inbox and connection data.

Mitigation: Use a dedicated browser profile where possible, share the LinkedIn tab only while actively using the skill, and unshare the tab when finished.

Risk: Automating LinkedIn may trigger service challenges, restrictions, or account bans.

Mitigation: Keep crawl sizes small, avoid large --top values, respect the built-in pacing and daily counters, and stop if LinkedIn returns a challenge or rate limit.

Risk: The security evidence flags a legacy-session check that may still load an old session secret despite documentation saying no old secret is read.

Mitigation: Review the session status and keychain cleanup behavior before relying on the no-secret-read claim, and run legacy cleanup deliberately after upgrading from older versions.

Risk: Optional caching can store crawled third-party LinkedIn profile or company data on disk.

Mitigation: Leave LINKEDIN_CACHE disabled unless caching is necessary; if enabled, keep the cache lifetime short and use session logout to remove local cached data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/linkedin-hack)
- [TinkerClaw project homepage](https://github.com/globalcaos/tinkerclaw)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [CLI JSON and plain text, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node and a locally shared LinkedIn browser tab through the OpenClaw relay.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
