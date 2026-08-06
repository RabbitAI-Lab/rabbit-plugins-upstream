## Description: <br>
Systematic backlink-building guidance for indie founders across Wikipedia and Wikidata preparation, public relations, review-site submissions, Reddit and Quora participation, HARO-style expert responses, and backlink auditing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gingiris-1031](https://clawhub.ai/user/gingiris-1031) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External founders, growth operators, and developer-marketing teams use this skill to plan backlink campaigns, prepare platform submissions, draft expert-response templates, and audit existing backlinks. It is intended for manual, policy-aware public SEO and reputation work rather than automated posting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides public SEO, reputation, review-site, Wikipedia, Wikidata, Reddit, Quora, and HARO-style actions that can violate platform rules or disclosure expectations if used carelessly. <br>
Mitigation: Review every public action manually, follow each platform's conflict-of-interest, paid-editing, disclosure, review, and anti-manipulation rules, and do not use fake reviews, undisclosed sponsorship, sockpuppets, or bought links. <br>
Risk: The audit script can make network requests and can send the target domain to DataForSEO when DATAFORSEO_B64 is configured. <br>
Mitigation: Run the audit only for domains you are authorized to analyze, unset DATAFORSEO_B64 unless paid DataForSEO use is intentional, and inspect known-links inputs before running verification. <br>
Risk: Platform availability, channel quality, and SEO/GEO assumptions can change over time. <br>
Mitigation: Verify current platform availability, submission requirements, and outreach policies before scheduling work or submitting content. <br>


## Reference(s): <br>
- [gr-backlinks ClawHub skill page](https://clawhub.ai/gingiris-1031/skills/gr-backlinks) <br>
- [Skill instructions](artifact/gr-backlinks/SKILL.md) <br>
- [Backlinks status ledger](artifact/data/backlinks-status.md) <br>
- [Wikipedia preparation template](artifact/gr-backlinks/templates/wikipedia-prep.md) <br>
- [HARO response template](artifact/gr-backlinks/templates/haro-response.md) <br>
- [Reddit and Quora playbook](artifact/gr-backlinks/templates/reddit-quora.md) <br>
- [Backlinks audit script](artifact/gr-backlinks/scripts/backlinks-audit.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, reusable templates, form-ready submission copy, shell commands, and JSON audit output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The audit script can use Common Crawl and can optionally call DataForSEO when DATAFORSEO_B64 is set; public submissions and community actions require manual review.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
