## Description: <br>
Query crypto project details, Web3 investor info, funding rounds, trending projects, and personnel job changes from RootData. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rdquanyu](https://clawhub.ai/user/rdquanyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to answer questions about crypto projects, Web3 investors, recent funding rounds, trending projects, and public personnel movements using RootData. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts RootData, creates a local anonymous API key, and retrieves public crypto-industry profile and personnel data. <br>
Mitigation: Use it only where outbound RootData API access and local ROOTDATA_SKILL_KEY storage are acceptable, and treat returned person or job-change information responsibly before sharing or acting on it. <br>
Risk: Returned profile, funding, investor, or personnel data could be used in outreach, compliance, hiring, or investment decisions without enough context. <br>
Mitigation: Verify important claims against source links or other authoritative sources and apply human review before using the data for consequential decisions. <br>


## Reference(s): <br>
- [RootData](https://www.rootdata.com) <br>
- [RootData Crypto Skill on ClawHub](https://clawhub.ai/rdquanyu/skills/rootdata-crypto) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with JSON request examples and summarized API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ROOTDATA_SKILL_KEY; first use may create a local anonymous RootData API key. Funding data is limited to the past 365 days, funding round investors are capped at three, and personnel job changes are capped at 20 recent entries per category.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence, released 2026-07-10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
