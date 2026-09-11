## Description:

Extract normalized content from public share URLs, RSS/Atom feeds, timed-text/subtitle documents, and web pages using a protocol-first fallback ladder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wuaishare](https://clawhub.ai/user/wuaishare)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ShareXtract to retrieve and normalize already-public web, feed, media metadata, subtitle, and AI-share content while preserving extraction provenance and avoiding authenticated or access-control-bypass workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted URLs or extracted page content could be treated as executable instructions.

Mitigation: Pass each URL only as one shell-free argv element and keep extracted remote content quoted as untrusted data unless the user independently requests a downstream action.

Risk: The skill depends on a separately provisioned runtime and network access for public retrieval.

Mitigation: Use only environments where ShareXtract v0.23.4 is already trusted and installed; stop instead of installing, upgrading, or enabling runtime components during skill execution.

Risk: Authenticated, private, paywalled, CAPTCHA-protected, or access-controlled content may be requested.

Mitigation: Use the skill for public URLs only and stop rather than bypass login walls, CAPTCHAs, paywalls, WAF challenges, private links, or other access controls.

## Reference(s):

- [ShareXtract ClawHub Skill Page](https://clawhub.ai/wuaishare/skills/sharextract)
- [Platform Matrix and Extraction Policy](references/platform-matrix.md)
- [Adapter Health and Fixture Corpus](references/adapter-health.md)
- [Adding an Adapter](references/adding-adapters.md)
- [Ecosystem Map](references/ecosystem.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured argv examples and JSON output-contract descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for invoking a pre-provisioned ShareXtract runtime against one public URL and interpreting normalized extraction fields such as source_url, canonical_url, extraction_method, confidence, text, markdown, metadata, warnings, and retrieved_at.]

## Skill Version(s):

0.23.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
